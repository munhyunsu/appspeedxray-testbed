import sqlite3
import configparser

from flask import Flask, request
from flask_restful import Resource, Api, reqparse


class Registration(Resource):
    def post(self):
        headers = request.headers()
        data = request.get_json()


    def get(self):
        identify = request.args.get('id')
        
