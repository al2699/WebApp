from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import pandas as pd
from Crime import Crime
import csv

fileName == 'crimes.csv'


app = Flask(__name__, template_folder=".")
GoogleMaps(app)

crimes = [getRowAmount(fileName)]

def getRowAmount(fileName):
  df = pd.read_csv(fileName)
  return df.shape[0]

def makeCrimeObjectsFromFile():
  df = pd.read_csv('crimes.csv')
  crimes[0] = Crime(df.Name[0], df.Date[0], df.Type[0], df.Location[0])
  """
  for x in range(0,1):
    crimes[x] = Crime(df.Name[x], df.Date[x], df.Type[x], df.Location[x])
  """
#Main page to display map
@app.route("/")
def mapview():
    # creating a map in the view
    #crime1 = Crime("DRUNK IN PUBLIC", "05/02/2017 06:00 AM", "DRUGS, COMBO OR TOLUENE (M)")
    makeCrimeObjectsFromFile()
    mymap = Map(
        identifier="view-side",
        lat=37.4419,
        lng=-122.1419,
        markers=[(37.4419, -122.1419)]
    )

    circle = {
        'stroke_color': '#FF00FF',
        'stroke_opacity': 1.0,
        'stroke_weight': 7,
        'fill_color': '#FFFFFF',
        'fill_opacity': .8,
        'center': {
                  'lat': 33.685,
                  'lng': -116.251
        },
        'radius': 2000,
    }

    circlemap = Map(
        identifier="circlemap",
        varname="circlemap",
        lat=33.678,
        lng=-116.243,
        circles=[
            circle,
            [33.685, -116.251, 1000],
            (33.685, -116.251, 1500),
        ]
    )

    sndmap = Map(
        identifier="sndmap",
        lat=33.200667,
        lng=-117.242767,
        circles=[
            circle,
            [33.200667, -117.242767, 1000],
            (33.200667, -117.242767, 1500),
        ],
        markers=[
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/green-dot.png',
             'lat': 33.201628,
             'lng': -117.242768,
             'infobox': "<b>" + crimes[0].getCrimeName() +":" + crimes[0].getCrimeType() + crimes[0].getCrimeDate()+ "</b>"
          },
          {
             'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
             'lat': 37.4300,
             'lng': -122.1400,
             'infobox': "<b>Hello World from other place</b>"
          }
        ],
        polylines = [{
            'stroke_color': '#ff0000',
            'stroke_opacity': 0.40,
            'stroke_weight': 5,
            'path': [
                (33.200658, -117.242769),
                (33.197153, -117.239464)
            ],
            'infobox': 'Crime Most Likely to occur: Property Crime\n Property Crimes: 40%\n Lancery Theft: 23.8%\n Violent Crimes: 10%\n Burglary: 10%\n Forcible Rape: 7%\n Aggrivated Assault: 6%\n 14% Other'
        }]
    )
    return render_template('example.html', mymap=mymap, sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)
