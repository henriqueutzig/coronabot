

class Tweet:
    
    def __init__(self, totalDeaths, totalInfected):
        if(totalInfected > 0 and totalDeaths > 0):
            self.text = "COVID-19 NO BRASIL\n\n"
            self.text += f"Infectados: {totalInfected:,}\nMortos: {totalDeaths:,}\n\n"
            self.text += "Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários Brasil.IO\n"
            self.text += "#FiqueEmCasa"

    def update(self, totalDeaths, totalInfected):
        self.text = ""
        if(totalInfected > 0 and totalDeaths > 0):
            self.text = "COVID-19 NO BRASIL\n\n"
            self.text += f"Infectados: {totalInfected:,}\nMortos: {totalDeaths:,}\n\n"
            self.text += "Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e equipe de voluntários Brasil.IO\n"
            self.text += "#FiqueEmCasa"

    def isDuplicated(self, oldTweets):
        isDup = True
        # remove current tweet footer 
        currentTweet = self.text[:self.text.find("Fonte")]
        # remove old tweet's footer 
        tweetsText = []
        for t in oldTweets:
            # remove tweet footer 
            text = t.full_text[:t.full_text.find("Fonte")]
            tweetsText.append(text)
        
        # compare current tweet text with old's text 
        if (currentTweet not in tweetsText):
            isDup = False

        return isDup
        