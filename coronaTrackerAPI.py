# Getting data from:  'https://covid19.mathdro.id/api'
import requests 
import json

import datetime
import os
from database import storeData

# Get Date 
currentDate = datetime.datetime.now().strftime('%Y-%m-%d')

def getLatestData():

    url = "https://covid19.mathdro.id/api/countries/BR"  # "https://api.covid19api.com/summary"

    payload = {}
    headers= {}

    response = requests.request("GET", url, headers=headers, data = payload)
    
    responseJson = json.loads(response.text)

    return responseJson