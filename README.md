# Crypto-Lister-API🏴

A simple Flask API for the crypto-lister application. The purpose of this repo is to serve as source code for my API at PythonAnywhere. 
The need for this service is that the WSGI configuration file is generated automatically by it.

## Instructions📜

This public API is hosted at: https://miguelartioli.pythonanywhere.com/

It has a few endpoints:

🚩 /get-currencies/ (GET), which returns data for all currencies.

🚩 /vote/<currency_name> (PUT), which increments votes for given currency by 1 and returns data for the updated currency.

🚩 /clear-votes (POST), which resets votes at 0 for all currencies.

## Concepts Applied🏴

- Flask API.
- SQLite3 database.
