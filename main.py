from flask import Flask, jsonify, render_template, request, Response
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# mysql+mysqlconnector://<user>:<password>@<host>[:<port>]/<dbname>
engine = create_engine('mysql+mysqlconnector://root:XWu10KhJPB#9uT@localhost:3307/sakila')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/descargar_reporte')
def descargar_reporte():
    query = "SELECT * FROM actor"
    df = pd.read_sql_query(query, con=engine)
    df.set_index('actor_id',inplace=True)
    print(df)
    return Response(df.to_csv(),mimetype="text/csv",headers={'Content-Disposition':'attachment; filename="actor_report.csv'})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
