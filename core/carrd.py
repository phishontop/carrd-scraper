import httpx


class Carrd:
    
    def __init__(self, name):
        self.name = name
        self.http()
        
    def http(self):
        self.request = httpx.get(f"https://{self.name}.carrd.co/")
        
    def isTaken(self):
        if self.request.status_code == 200:
            return True
        else:
            return False
        
    def getHtml(self):
        return self.request.text
