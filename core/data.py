import json
import re


class Data:
    
    def __init__(self, words):
        self.words = words
        self.data = self.readFile()
        self.dataFound = {}

    def readFile(self):
        return json.load(open("data.json"))
    
    def find_all_words(self, words, sentence):
        all_words = re.findall(r'\w+', sentence)
        words_found = []
        for word in words:
            if word in all_words:
                words_found.append(word)
                
        return words_found
    
    def scrapeData(self):
        for info in self.data:
            for line in self.words:
                results = self.find_all_words(info["keywords"], line)
                if len(results) > 0:
                    try:
                        self.dataFound[info["type"]] += len(results)
                    except:
                        self.dataFound[info["type"]] = len(results)
        return self.dataFound            
