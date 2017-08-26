from __future__ import unicode_literals
from flask import Flask, request, jsonify, make_response
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import json
import requests
import hashlib, uuid
import calendar
import time

class API():

    # Initialize api server configurations, cors is needed for cross browser calling
    app = Flask('fleet_server')
    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Initialize database configurations
    mongo_config = {
        'host': 'localhost',
        'port': 27017
    }
    mongo = MongoClient(mongo_config['host'],int(mongo_config['port']))

    def validate_user(self,user):
        print user
        return True

    def __init__(self):
        pass


    # Register method, when users log in with JSON, register user to mongo database
    @staticmethod
    @app.route('/api/v1.0/register', methods=['POST'])
    def fleet_register():
        user = request.json['user']
        password = request.json['pass']
        time_now = calendar.timegm(time.gmtime())
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password + salt).hexdigest()
        email = request.json['email']
        user_fullname = request.json['user_fullname']

        if API.validate_user(user) is False:
            print "User already exists"
        else:
            print "user exists!"



        results = {}
        return jsonify({'result': results})


    # If 404 error, handle it gracefully
    @staticmethod
    @app.errorhandler(404)
    @cross_origin()
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)

    # Run the api server
    def run(self,debug=False,port=5000):
        self.app.run(port=port, debug=debug,host='0.0.0.0', threaded=True)


ab = API()
ab.run(True)