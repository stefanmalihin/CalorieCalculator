import requests
from selectorlib import Extractor


class Temperature:

    def __init__(self, city, country):
        self.country = country
        self.city = city

    def get(self):
        r = requests.get(f"https://www.timeanddate.com/weather/{self.country}/{self.city}")
        c = r.text
        extractor = Extractor.from_yaml_file('temperature.yaml')
        raw_result = extractor.extract(c)
        result = raw_result['temp'].replace("\xa0°C", "")
        return result
