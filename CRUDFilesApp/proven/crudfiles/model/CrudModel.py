import os

class CrudModel:
    def createFile(self, filepath) -> bool:
        cond = False
        
        if open(filepath, "x"):
            cond = True
        return cond
    
    def readFile(self, filepath) -> str:
        try:
            fileRead = open(filepath, "r").read()
        except:
            return ""
            
        return fileRead
    
    def writeFile(self, filepath, text: str):
        #TODO: Improve this method by reading as well
        try:
            fileWrite = open(filepath, "w")
            fileWrite.write(text)
            return True
        except:
            return False
        
    def removeFile(self, filepath) -> bool:
        try:
            os.remove(filepath)
        except:
            return False
        return True
    
    