import os

class CrudModel:
    def createFile(self, filepath) -> bool:
        """Creates a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            bool: True if added, otherwise False
        """
        cond = False
        
        if open(filepath, "x"):
            cond = True
        return cond
    
    def readFile(self, filepath) -> str:
        """Reads a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            str: Returns the text obtained with the read() option
        """
        try:
            fileRead = open(filepath, "r").read()
        except:
            return ""
            
        return fileRead
    
    def writeFile(self, filepath, text: str):
        """Writes an existing file or creates one if not

        Args:
            filepath (str): Text of the filepath to create a file
            text (str): Given text to add

        Returns:
            bool: True if added, otherwise False
        """
        try:
            fileWrite = open(filepath, "a")
            fileWrite.write(text + "\n")
            
            return True
        except:
            return False
        
    def removeFile(self, filepath) -> bool:
        """Removes a file with the filepath str given

        Args:
            filepath (str): Text of the filepath to create a file

        Returns:
            bool: True if removed, otherwise False
        """
        try:
            os.remove(filepath)
        except:
            return False
        return True