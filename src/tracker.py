# Getting data from:  brasil.io
import requests
import json
import pandas as pd 


class Tracker:
    apiUrl = 'https://brasil.io/api/dataset/covid19/caso/data/?format=json&is_last=True&place_type=state'
    
    def __init__(self):
        self.dfRes = self.callApi()

        self.totalDeaths = self.dfRes['deaths'].sum()
        self.totalInfected = self.dfRes['confirmed'].sum()
        
    def callApi(self):
        apiRes = requests.request("GET", self.apiUrl)
        jsonRes = json.loads(apiRes.text)

        dfRes = pd.DataFrame.from_records(jsonRes['results'])
        return dfRes

    def update(self):
        self.dfRes = self.callApi()

        self.totalDeaths = self.dfRes['deaths'].sum()
        self.totalInfected = self.dfRes['confirmed'].sum()

    def getTotalDeaths(self):
        return self.totalDeaths

    def getTotalInfected(self):
        return self.totalInfected
