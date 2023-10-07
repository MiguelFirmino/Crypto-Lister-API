from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app) # Way of solving Access-Control-Allow-Origin problem

@app.route("/get-currencies")
def get_all_currencies():
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    # Not recommended if using large databases, but fine for this instance
    query = '''SELECT name, votes 
               FROM currencies
               ORDER BY votes DESC'''
    result = cursor.execute(query).fetchall()

    return jsonify(result)

@app.route("/vote/<currency_name>", methods=["PUT"])
def increase_vote(currency_name):
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    query = f'''UPDATE currencies
                SET votes = votes + 1
                WHERE name = "{currency_name}"'''
    result = cursor.execute(query)
    connection.commit()

    return f"Increased votes of: {currency_name}" # Not sure

@app.route("/clear-votes", methods=["POST"])
def clear_votes():
    connection = sqlite3.connect('currencies.db')
    cursor = connection.cursor()

    query = f'''UPDATE currencies
                SET votes = 0'''
    cursor.execute(query)
    connection.commit()

    return # Not sure

if __name__ == "__main__":
    app.run(debug=True)