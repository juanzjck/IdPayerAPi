import json
import js2py
import sys
import falcon
from Naked.toolshed.shell import execute_js, muterun_js
from twilio import twiml
from flask import  Flask, request
from flask_restful import  Api, Resource, reqparse
app=Flask(__name__)
api=Api(app)
db = [{"Valor":"2","idpos":"12sd","huella":"adasd"},{"Valor":"20","idpos":"12sd","huella":"sdas334"}]

class pos(Resource):


    # print(str(decoded["Pos"][0]["Info"][0]["Valor"]) + str(decoded["Pos"][0]["Info"][0]["id_pos"]) + str(
    # decoded["Pos"][0]["Info"][0]["huella"]))

    #resive el jsnon lo lee y lo interpreta con javascript


    def post(self, data):
        parser= reqparse.RequestParser()
        parser.add_argument("Valor")
        parser.add_argument("idpos")
        parser.add_argument("huella")
        args= parser.parse_args()
        resp=''
        entry_pos={"Valor":args["Valor"],"idpos":args["idpos"],"huella":args["huella"]}
       # db.append(entry_pos)
        for d in db:
            #print(d["Valor"])
            if d["huella"] == args["huella"]:

                resp='Succesful,valor:'+args["Valor"]
            else:

             resp = 'fail'



        # encoded
        # data_string = json.dumps(data)

        # Decoded
        #decoded = json.loads(data)
        print(data)
        print(resp)
        #print(str(decoded["Pos"][0]["Info"][0]["Valor"]))
        #===========
        #response = muterun_js('Xchange.js')
        # if response.exitcode == 0:
        #     print(response.stdout)
        # else:
        #    sys.stderr.write(response.stderr)
        #===========


        return resp
class posr(Resource):
    def hola(self):
        print('hola')
api.add_resource(pos,'/pos/<string:data>')
api.add_resource(posr,'/pos2/<string:data>')
app.run(debug=True)