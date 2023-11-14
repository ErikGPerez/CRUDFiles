import os

class CrudModel:
    #TODO Comment and implement all the defs to work with files
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
    
    def writeFile(self, filepath):
        open(filepath, "w")
        pass
    
    def removeFile(self, filepath):
        os.remove(filepath)
        pass
    
    