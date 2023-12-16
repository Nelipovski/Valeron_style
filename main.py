from http.server import BaseHTTPRequestHandler, HTTPServer

from datetime import datetime

import psycopg2

import json

import logging

logging.basicConfig(level=logging.INFO, filename='first_log.log')
####
#
#

sql1 = '''CREATE TABLE IF NOT EXISTS users (
id SERIAL PRIMARY KEY,
name VARCHAR(20) NOT NULL,
email VARCHAR(50) NOT NULL UNIQUE,
login VARCHAR(20) NOT NULL UNIQUE,
password VARCHAR(130) NOT NULL
);'''


def sql_func(sql: str):
    conn = psycopg2.connect(
        dbname="pg_db", host="localhost", user="admin", password="password", port="5434")

    conn.autocommit = True  # устанавливаем актокоммит

    cursor = conn.cursor()
    cursor.execute(sql)
    # непосредственное выполнение команды sql1

    cursor.close()

    conn.close()
#####
#####
#####


sql_func("CREATE TABLE IF NOT EXISTS peoples (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")
sql_func("CREATE TABLE IF NOT EXISTS peoples1 (id SERIAL PRIMARY KEY, name VARCHAR(50),  age INTEGER)")

PORT_NUMBER = 8080

# This class will handle any incoming request from
# a browser


class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the html message

        now = datetime.now()
        time = now.strftime('%H:%M:%S')
        time_dict = {
            'time': time
        }
        time_dict = json.dumps(time_dict)
        self.wfile.write(bytes(time_dict, "utf-8"))
        logging.info(f'{time_dict}')


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ', PORT_NUMBER)

    # Wait forever for incoming http requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
