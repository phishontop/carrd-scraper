from core import Carrd, Scrape, Data

name = input("Enter carrd name you want to scrape -> ")

carrd = Carrd(name=name)
carrdTaken = carrd.isTaken()
carrdHtml = carrd.getHtml()

scrape = Scrape(html=carrdHtml)
scrapeLinks = scrape.getLinks()
scrapeText = scrape.getText()

data = Data(words=scrapeText)
dataScraped = data.scrapeData()


print("Keywords/Info Found")
for dataKey in dataScraped.keys():
    print(f"{dataKey}: {dataScraped[dataKey]}")
    
print("Links Found")
for link in scrapeLinks:
    print(link)
