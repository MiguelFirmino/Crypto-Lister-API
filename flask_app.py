from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app) # Way of solving Access-Control-Allow-Origin problem

@app.route("/")
def home():
    return "Hello, you're at home!"

@app.route("/get-currencies")
def get_all_currencies():
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    # Not recommended if using large databases, but fine for this instance
    query = '''SELECT name, votes, icon_link
               FROM currencies
               ORDER BY votes DESC'''
    result = cursor.execute(query).fetchall()

    return jsonify(data= result)

@app.route("/vote/<currency_name>", methods=["PUT"])
def increase_vote(currency_name):
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    # Increases currency vote by 1
    query = f'''UPDATE currencies
                SET votes = votes + 1
                WHERE name = "{currency_name}"'''
    cursor.execute(query)
    connection.commit() # Saves changes

    # Gets updated currency values
    query = f'''SELECT name, votes, icon_link
                FROM currencies
                WHERE name = "{currency_name}"'''
    result = cursor.execute(query).fetchall()[0] # Gets first occurance item from query

    return jsonify(data= result)

@app.route("/clear-votes", methods=["POST"])
def clear_votes():
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    query = '''UPDATE currencies
                SET votes = 0'''
    cursor.execute(query)
    connection.commit()

    return "Cleared all votes"

#if __name__ == "__main__":
#    app.run(debug=True)