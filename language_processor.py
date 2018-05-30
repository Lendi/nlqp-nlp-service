from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu import config
from rasa_nlu.model import Trainer, Metadata, Interpreter
import os

config_location = "./config_spacy.json"
model_directory = ""
def train_processor(training_data, config_dir):
	global config_location, model_directory
	config_location = config_dir
	training_data = load_data(training_data)
	print(config_dir)
	trainer = Trainer(config.load(config_dir))
	trainer.train(training_data)
	model_directory = trainer.persist(os.path.join(os.path.dirname(__file__), './nlu/sample/default/'))

def interpret_data_for(text_to_be_parsed, user_name="User"):
	metadata = Metadata.load(model_directory)
	interpreter = Interpreter.load(model_directory)
	interpreted_data = interpreter.parse(text_to_be_parsed.decode('utf-8'))
	return get_response_for(interpreted_data, user_name)

def get_response_for(interpreted_data, user_name="User"):
	intent = interpreted_data['intent']['name']
	print(intent)
	if(intent == u"greet"):
		return "Hello! Hope you are having a good day"
	elif(intent == u"inventory_search"):
		entity = interpreted_data['entities'][0]['value']
		if entity == "inventory_type":
			return "Hold on, looking for " + str(entity) + ".."
		elif entity == "inventory_storage":
			return "Hold on, let me have a look at " + str(entity) + ".."
	else:
		return "Cant understand the query"
