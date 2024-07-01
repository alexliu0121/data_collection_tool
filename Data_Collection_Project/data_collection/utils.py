import json
import logging
import os

def save_to_json(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        handlers=[logging.FileHandler('data_collection.log'),
                                  logging.StreamHandler()])
    return logging.getLogger('DataCollectionTool')
