from flask import Flask
from flask_restful import Resource, Api, reqparse
from SparqlWrapper import SparqlWrapper

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
sw = SparqlWrapper()
FUSEKI = '172.18.0.1'  

class SensorInsert(Resource):
    def post(self):
        # parser.add_argument('data')
        # args = parser.parse_args()
        insert = getattr(sw,'insert')
        result = insert(FUSEKI)
        return result 

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

# Run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)