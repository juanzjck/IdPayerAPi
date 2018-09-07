
#dependens
from flask import  Flask
from flask_restful import  Api
from Classes import DataBase
from Classes.DataBase import DataBase
app=Flask(__name__)
api=Api(app)
#clasess
from Classes import Pos
from Classes.Pos import Pos
def main():
    db = DataBase("Jack1996jack", "IdPayer")
    #paths
    api.add_resource(Pos, '/pos/<string:option>',resource_class_kwargs={ 'connection': db })
    app.run(debug=True)

if __name__ == "__main__": main()

