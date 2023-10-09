from flask import Flask, jsonify
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app) # Way of solving Access-Control-Allow-Origin problem

@app.route("/")
def home():
    # Test route
    return "Hello, you're at home!"

@app.route("/get-currencies")
def get_all_currencies():
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    # Not recommended if using large databases, but fine for this instance
    query = '''SELECT name, votes, icon_link, aka
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
    query = f'''SELECT name, votes, icon_link, aka
                FROM currencies
                WHERE name = "{currency_name}"'''
    result = cursor.execute(query).fetchall()[0] # Gets first occurance item from query

    return jsonify(data= result)

@app.route("/remove-vote/<currency_name>", methods=["PUT"])
def decrease_vote(currency_name):
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    # Decreases currency vote by 1 if votes > 0
    query = f'''UPDATE currencies
            SET votes = votes - 1
            WHERE name = "{currency_name}" AND votes > 0'''

    # Gets updated currency values
    # note: i've decided not to put this into a function so 
    # as to not make another database connection.
    query = f'''SELECT name, votes, icon_link, aka
                FROM currencies
                WHERE name = "{currency_name}"'''
    result = cursor.execute(query).fetchall()[0] # Gets first occurance item from query
    


@app.route("/clear-votes", methods=["POST"])
def clear_votes():
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    query = '''UPDATE currencies
                SET votes = 0'''
    cursor.execute(query)
    connection.commit()

    return "Cleared all votes"

# not needed for PythonAnywhere applications
# if __name__ == "__main__":
#    app.run(debug=True)