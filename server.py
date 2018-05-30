from flask import Flask
from flask_restplus import Resource, Api, fields
from flask_cors import CORS, cross_origin
from language_processor import train_processor, interpret_data_for
import os

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
		result = interpret_data_for(query)
		return {'result':result}


if __name__ == "__main__":
    app.run(debug=True)
