import os.path
import json


def storeData(currentData):
    # rewrites oldJson file with currentData values
    with open('data.json', 'w') as wj:
        json.dump(currentData, wj, indent=4)

def compareData(currentData):
    isDifferent = False

    #check if oldJson File exists sand as data 
    if(os.path.isfile('data.json')):
        with open('data.json', 'r') as rj:
            rj_file = rj.read()
        oldData = json.loads(rj_file)

        if((currentData['confirmed'] != oldData['confirmed']) or 
        (currentData['recovered'] != oldData['recovered']) or 
        (currentData['deaths'] != oldData['deaths'])):
            isDifferent = True
            #print("~DATA IS DIFFERENT")
            # printCompare(currentData, oldData)
    else:
        storeData(currentData)

    return isDifferent



def printCompare(currentData, oldJson):
    print("Old      x           New")
    print("Infectados: " + str(oldJson['confirmed']['value']) + " | " + str(currentData['confirmed']['value']))
    print("Mortes: " + str(oldJson['deaths']['value']) + " | " + str(currentData['deaths']['value']))
    print("Recuperados: " + str(oldJson['recovered']['value']) + " | " + str(currentData['recovered']['value']))
    #print("Infectados: " + str(oldJson['lastUpdate']['value']) + " | " + str(currentData['lastUpdate']['value']))
    
    