from flask import Flask, request
from flask_restful import Resource, Api, reqparse

from deliver import Deliver
from register import Registration


def main():
    app = Flask(__name__)
    api = Api(app)

    api.add_resource(Deliver, '/')
    api.add_resource(Registration, '/res')


