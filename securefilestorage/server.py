import os
import psycopg2
from flask import Flask,render_template
app = Flask(__name__)
conn = psycopg2.connect(
    host='localhost', 
    database='PROTO1',
    user=os.environ['USERNAME'], 
    )
cur =conn.cursor()

@app.route('/login')
def login():
    return


@app.route('/')
def sfs():
    login()
    return 'okay 202 response'


if __name__ == '__main__':
    app.run()
