import requests
import pandas as pd
from abc import ABC, abstractmethod
from .utils import logger

class BaseScraper(ABC):
    def __init__(self, url, params):
        self.url = url
        self.params = params

    def fetch_data(self):
        try:
            response = requests.get(self.url, params=self.params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            logger.error(f"Error fetching data: {e}")
            return None

    @abstractmethod
    def parse_data(self, raw_data):
        pass

    def save_data(self, data, file_path):
        try:
            data.to_csv(file_path, index=False)
            logger.info(f"Data saved to {file_path}")
        except Exception as e:
            logger.error(f"Error saving data: {e}")

    def run(self, file_path):
        raw_data = self.fetch_data()
        if raw_data:
            parsed_data = self.parse_data(raw_data)
            self.save_data(parsed_data, file_path)
