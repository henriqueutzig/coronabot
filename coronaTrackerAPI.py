# Getting data from:  brasil.io
import requests
import json
import pandas as pd 

global dfData

def getLatestData():

    url = 'https://brasil.io/api/dataset/covid19/caso/data/?format=json&is_last=True&place_type=state'

    apiResponse = requests.request("GET", url)
    
    responseJson = json.loads(apiResponse.text)
    jsonList = responseJson['results']

    global dfData
    dfData = pd.DataFrame.from_records(jsonList)

    return responseJson

def getTotalDeaths():
    return dfData['deaths'].sum()

def getTotalInfected():
    return dfData['confirmed'].sum()

#def getStateDeaths(state):
#
#    return deaths
#
#def getStateInfected(state):
#
#    return infected