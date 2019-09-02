from flask import Flask, request
from flask_restful import Resource, Api, reqparse


class AppSpeedXrayTestBed(Resource):
    def post(self):
        pass


def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(App)
