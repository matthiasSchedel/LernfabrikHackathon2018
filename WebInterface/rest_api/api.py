from flask import Flask
from flask_restful import Resource, Api, reqparse
from SparqlWrapper import SparqlWrapper
from MessageHandler import MessageHandler

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
sw = SparqlWrapper()
mh = MessageHandler()
FUSEKI = '172.18.0.1'  

class UpdateClients(Resource):
    def post(self):
        # parser.add_argument('data')
        parser.add_argument('author')
        args = parser.parse_args()
        update = getattr(mh,'updateClients')
        result = update()
        return result 
class SensorInsert(Resource):
    def post(self):
        # parser.add_argument('data')
        # args = parser.parse_args()
        insert = getattr(sw,'insert')
        result = insert(FUSEKI)
        return result 

class Test(Resource):
    def get(self):
        return {"test":"a"} 

class SensorData(Resource):
    def post(self):
        parser.add_argument('foo')
        parser.add_argument('int_bar', type=int)
        args = parser.parse_args()
        request = getattr(sw,'request')
        result = request(FUSEKI)
        return result

# Create routes
api.add_resource(SensorData, '/sensor')
api.add_resource(SensorInsert, '/insert')
api.add_resource(Test, '/test')
api.add_resource(UpdateClients, '/updateClients')

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)