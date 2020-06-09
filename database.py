import os.path
import json


def storeData(currentData):
    # rewrites oldJson file with currentData values
    with open('data.json', 'w') as wj:
        json.dump(currentData, wj, indent=4)

# just compares the fetch json with the one save in the machine
# still not a good comparation, but it works for now 
def compareData(currentData):
    isDifferent = False

    #check if oldJson File exists sand as data 
    if(os.path.isfile('data.json')):
        with open('data.json', 'r') as rj:
            rj_file = rj.read()
        oldData = json.loads(rj_file)

        if(currentData != oldData):
            isDifferent = True
    else:
        storeData(currentData)
        isDifferent = True
    #print("isDifferent: " + str(isDifferent))
    return isDifferent
