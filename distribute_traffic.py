#!/usr/bin/env python

from api import *
from m2wsgi.io.standard import WSGIHandler, Connection
import webapp2
routes = [('/api/distribute_traffic', DitributeTrafficAPI)]

app = webapp2.WSGIApplication(routes, debug=True)
conn = Connection(send_sock="tcp://127.0.0.1:9991", recv_sock="tcp://127.0.0.1:9992")
handler = WSGIHandler(app,conn)

def main():
    print("Ready")
    handler.serve()

if __name__ == "__main__":
    main()
