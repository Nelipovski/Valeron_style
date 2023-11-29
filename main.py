from http.server import BaseHTTPRequestHandler, HTTPServer

from datetime import datetime

import requests

import json

import logging

logging.basicConfig(level=logging.INFO, filename='first_log.log')


PORT_NUMBER = 8080

# This class will handle any incoming request from
# a browser


class myHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        path = self.path

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # Send the html message

        if path == '/Time':
            now = datetime.now()
            time = now.strftime('%H:%M:%S')
            time_dict = {
                'time': time
            }
            time_dict = json.dumps(time_dict)
            self.wfile.write(bytes(time_dict, "utf-8"))
            logging.info(f'{time_dict}')

        elif path == '/Index':
            response = requests.get('Valeron_style/index.html')
            self.wfile.write(bytes(response.text, 'utf-8'))


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
