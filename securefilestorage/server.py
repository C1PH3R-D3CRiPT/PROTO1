import os
from elasticsearch import Elasticsearch
from flask import Flask, render_template, request

app = Flask(__name__)
es = Elasticsearch(hosts=[{'host': 'https://localhost', 'port': 9200}])
index = 'customer_details'

@app.route('/login')
def login():
    if request.method == POST:
        email = request.form['email']
        password = request.form['password']

        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"username.keyword": username}},
                        {"term": {"password.keyword": password}}
                    ]
                }
            }
        }

        response = es.search(index=index_name, body=query)
        if response['hits']['total']['value'] == 1:
            # Login successful, redirect to a protected page
            return "Login successful!"
        else:
            # Login failed, show an error message
            return "Invalid credentials!"
    return render_template('login.html')


@app.route('/register')
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username already exists

        query = {
            "query": {
                "bool": {
                    "must": [
                        {"term": {"username.keyword": username}}
                    ]
                }
            }
        }

        response = es.search(index=index_name, body=query)

        if response['hits']['total']['value'] > 0:
            # Username already exists, show an error message
            return "Username already exists!"

        # Create a new user document in Elasticsearch
        user_doc = {
            'username': username,
            'password': password
        }

        es.index(index=index_name, body=user_doc)

        # Registration successful, redirect to the login page
        return "Registration successful! Please log in."

    return render_template('register.html')


if __name__ == '__main__':
    app.run()
