import os.path
import json


class Tweet:
    
    def __init__(self, totalDeaths, totalInfected):
        if(totalInfected > 0 and totalDeaths > 0):
            self.tweet = "COVID-19 NO BRASIL\n\n"
            self.tweet += f"Infectados: {totalInfected:,}\nMortos: {totalDeaths:,}\n\n"
            self.tweet += "Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários Brasil.IO\n"
            self.tweet += "#FiqueEmCasa"

    def isDuplicated(self, oldTweets):
        isDup = True



        return isDup
        
