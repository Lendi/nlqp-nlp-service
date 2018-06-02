from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_cors import CORS, cross_origin
from language_processor import train_processor, interpret_query_for
from querycsv import query_csv
import os

CSV_DATABASE=['./population.csv']

print "Starting language processor..."
train_processor(os.path.join(os.path.dirname(__file__), 'nlu/training_data.json'), os.path.join(os.path.dirname(__file__), 'nlu/config.yml'))
print "Ended training dataset. Ready to take the hit..."

app = Flask(__name__)
api = Api(app)
CORS(app)

@api.route('/index')
class Home(Resource):
    def get(self):
        return {'hello': 'world'}

@api.route('/nlpQuery/<string:query>')
class QueryResource(Resource):
	def get(self, query):
        	result_query = interpret_query_for(query)
        	dummy_query = 'select count(*) from population'
        	result_data = query_csv(dummy_query, CSV_DATABASE[0])
        	return { 'result_query': result_query, 'result_data': result_data}


if __name__ == "__main__":
    app.run(debug=True)
