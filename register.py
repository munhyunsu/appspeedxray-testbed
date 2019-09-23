from flask import Flask, request
from fkask_restful import Resource, Api, reqparse


class Registration(Resource):
    def post(self):
        headers = request.headers
        data = request.get_json()
        pass

    def get(self):
        identify = request.args.get('id')
        pass
        
