import psycopg2

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Jasmine in 3308'

@app.route('/tests')
def db_test():
    conn = psycopg2.connect("postgresql://db00_f7md_user:dxLbuFZP3UsJPgrGK2h3dQEhOrCZAHeQ@dpg-cql4p32j1k6c739hm5q0-a/db00_f7md")
    conn.close()
    return "Database Connection Successful"
    
