import json
import js2py
import sys
from Naked.toolshed.shell import execute_js, muterun_js
from twilio import twiml
from flask import  Flask, request
from flask_restful import  Api, Resource, reqparse
db = [{"Valor":"2","idpos":"12sd","huella":"adasd","PIN":"asda"}]
from Classes import DataBase
from Classes.DataBase import DataBase
class Pos(Resource):
    def __init__(self, **kwargs):
        self.connection = kwargs['connection']


    #resive el jsnon lo lee y lo interpreta con javascript
    def post(self, option):
        parser= reqparse.RequestParser()
        parser.add_argument("Valor")
        parser.add_argument("idpos")
        parser.add_argument("huella")
        parser.add_argument("PIN")
        args= parser.parse_args()
        entry_pos={"Valor":args["Valor"],"idpos":args["idpos"],"huella":args["huella"],"PIN":args["PIN"]}
        resp= self.connection.Match("sdf", args["PIN"])
        if resp != 'NONE':

            resp = "succeful" + str(resp)

        else:
            resp = "fail"


        return resp
    #end of post


