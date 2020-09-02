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

    def getTotalDeaths(self):
        return self.totalDeaths

    def getTotalInfected(self):
        return self.totalInfected


trk = Tracker()
print(trk.getTotalDeaths())
print(trk.getTotalInfected())

# global dfData

# def getLatestData():

#     url = 'https://brasil.io/api/dataset/covid19/caso/data/?format=json&is_last=True&place_type=state'

#     apiResponse = requests.request("GET", url)
    
#     responseJson = json.loads(apiResponse.text)
#     jsonList = responseJson['results']

#     global dfData
#     dfData = pd.DataFrame.from_records(jsonList)

#     return responseJson

# def getTotalDeaths():
#     return dfData['deaths'].sum()

# def getTotalInfected():
#     return dfData['confirmed'].sum()

# def getStateDeaths(state):
#     return dfData['deaths'].where((dfData['state'] == state)).sum()

# def getStateInfected(state):
#     return dfData['confirmed'].where((dfData['state'] == state)).sum()