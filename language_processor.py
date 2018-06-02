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

def interpret_query_for(text_to_be_parsed, user_name="User"):
	# Example scenario:
	# text_to_be_parsed: 'what is the total population?'
	metadata = Metadata.load(model_directory)
	interpreter = Interpreter.load(model_directory)
	interpreted_data = interpreter.parse(text_to_be_parsed.decode('utf-8'))
	return get_structured_query(interpreted_data, user_name)

def get_structured_query(interpreted_data, user_name="User"):
	# Example scenario:
	# interpreted_data = { intent: 'some_search_operation', entities:[{total:'count'},{population:'table'}] }
	# given some_search_operation intent, and entities -> output should be SQL:"select count(*) from population"
	pass
