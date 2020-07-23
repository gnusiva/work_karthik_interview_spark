from flask import Flask
from flask import request
import sqlite3

from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"

@app.route('/exchangeData')
def exchangeData():
    currency = request.args.get('currency')
    return queryDatabase(currency)

def queryDatabase(currency):
    conn = sqlite3.connect('../03spark/test.db')
    c = conn.cursor()
    result = []
    qry = "SELECT * FROM currency  WHERE name='" + currency + "'"
    c.execute(qry)
    id = c.fetchone()[0]
    qry2 = "SELECT * FROM DailyExchange  WHERE currencyId='"+ str(id) +"' ORDER BY date LIMIT 1000"
    print(qry2)
    for row in c.execute(qry2):
        date = row[1]
        value = row[2]
        result.append([date, value])
    conn.close()
    resp = jsonify(result)
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return resp

if __name__ == '__main__':
    app.run()