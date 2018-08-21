import json

from flask import  Flask
from flask_restful import  Api, Resource, reqparse
app=Flask(__name__)
api=Api(app)
db = [{"Valor":"2","idpos":"12sd","huella":"adasd"}]

class pos(Resource):


   # print(str(decoded["Pos"][0]["Info"][0]["Valor"]) + str(decoded["Pos"][0]["Info"][0]["id_pos"]) + str(
    #    decoded["Pos"][0]["Info"][0]["huella"]))

    #resive el jsnon lo lee y lo interpreta con javascript

    def post(self, data):
        parser= reqparse.RequestParser()
        parser.add_argument("Valor")
        parser.add_argument("idpos")
        parser.add_argument("huella")
        args= parser.parse_args()

        entry_pos={"Valor":args["Valor"],"idpos":args["idpos"],"huella":args["huella"]}
        db.append(entry_pos)
        for d in db:
            print(d["Valor"])

        # encoded
      #  data_string = json.dumps(data)

        # Decoded
       # decoded = json.loads(data)
        print(data)
        #print(str(decoded["Pos"][0]["Info"][0]["Valor"]))

        return "succes"

api.add_resource(pos,'/<string:data>')
app.run(debug=True)