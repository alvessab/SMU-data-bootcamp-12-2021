#import dependencies
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine
from flask import Flask, jsonify

#create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#create an app
app = Flask(__name__)

# Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received the / request, or the listener was activated")
    return("""Welcome to a Hawaii climate app! Below are the routes available:
    <br>
    /api/v1.0/precipitation
    <br>
    /api/v1.0/stations
    <br>
    /api/v1.0/tobs
    <br>
    /api/v1.0/{start date} when date is formatted as YYYY-MM-DD  
    <br>
    /api/v1.0/{start date}/{end date} when date is formatted as YYYY-MM-DD
    """)


@app.route("/api/v1.0/precipitation")
def precipitation():
    try:

        query = """SELECT
                date, prcp
            FROM 
                measurement
            WHERE
                date >= '2016-08-23';"""

        conn = engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()
        data = df.to_dict(orient="records")
        return(jsonify(data))

    except Exception as e:
        error = {"Error: Page Can't Load"}
        return(jsonify(error))

@app.route("/api/v1.0/stations")
def stations():
    try:

        query = """SELECT
                DISTINCT station
            FROM 
                measurement;"""

        conn = engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()
        data = df.to_dict(orient="records")
        return(jsonify(data))

    except Exception as e:
        error = {"Error: Page Can't Load"}
        return(jsonify(error))

@app.route("/api/v1.0/tobs")
def tobs():
    try:

        query = """SELECT
                station,
                date,
                tobs
            FROM 
                measurement
            WHERE
                date >= '2016-08-23'
            AND
                station = 'USC00519281';"""

        conn = engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()
        data = df.to_dict(orient="records")
        return(jsonify(data))

    except Exception as e:
        error = {"Error: Page Can't Load"}
        return(jsonify(error))

@app.route("/api/v1.0/{start}/{end}")
def getTemp(start, end):
    try:

        query = """
        SELECT
            min(tobs) as tmin,
            max(tobs) as tmax,
            avg(tobs) as tavg
        FROM 
            measurement
        WHERE
            date >= '{start}'
            and date <= '{end}';"""

        conn = engine.connect()
        df = pd.read_sql(query, conn)
        conn.close()
        data = df.to_dict(orient="records")
        return(jsonify(data))

    except Exception as e:
        error = {"Error: Page Can't Load"}
        return(jsonify(error))




if __name__ == "__main__":
    app.run(debug=True)

