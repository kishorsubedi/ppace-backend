from flask import Flask
app = Flask(__name__)
import os
import pyodbc

@app.route("/")
def hello():
    return "Hello MANN!"

@app.route('/posts', methods=['GET'])
def home():
    a = getPostsFromDb()
    #console.log(posts)
    return "<h1>Queried Azure SQl Datbase in" + a + os.environ['testPathVariable'] + "kishor /get endpoint</h1><p>FIFI</p>"


def getPostsFromDb():
    server = 'ppacedbserver.database.windows.net'
    database = 'ppaceDb'
    username = 'kishbuy238'
    password = '238aZure'
    driver= '{ODBC Driver 17 for SQL Server}'
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    cursor.execute("SELECT * FROM dbo.Customers")
    row = cursor.fetchone()
    result = ""
    while row:
        result += (str(row[0]) + " " + str(row[1]))
        row = cursor.fetchone()
    return result