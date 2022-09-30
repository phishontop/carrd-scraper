from bs4 import BeautifulSoup
import re


class Scrape:
    
    def __init__(self, html):
        self.html = html
        self.soupHtml()
        
    def soupHtml(self):
        self.soup = BeautifulSoup(self.html, features="lxml")
        
    def getSoup(self):
        return self.soup
    
    def getLinks(self):
        links = []
        for soupLink in self.soup.find_all('a', href=True):
            link = soupLink["href"]
            if "http" in link and "carrd" not in link:
                links.append(link)
            
        return links
    
    def getTags(self, htmlElement):
        tags = [tag.name for tag in htmlElement]
        return tags
    
    def getText(self):
        textFound = []
        tags = []
        
        for carrdHtml in self.soup.find_all("div", {"class": "wrapper"}):
            innerHtml = carrdHtml.find("div", {"class": "inner"})
            tags.append({
                "html": innerHtml,
                "elements": self.getTags(innerHtml)
            })
        
        for i in range(2):
            newTags = []
            for i in tags:
                for html in i["html"].find_all(i["elements"]):
                    newTags.append({
                        "html": html,
                        "elements": self.getTags(html),
                        "text": html.text
                    })
            tags = newTags
        
        for i in tags:
            if i["text"] not in textFound:
                textFound.append(i["text"])
            
                        
        return textFound
