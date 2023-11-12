class Option:
    def __init__(self, text, actionCommand):
        self.text = text
        self.actionCommand = actionCommand
        
    def __hash__(self):
        prime = 31
        result = 1
        result = prime * result + (0 if self.actionCommand is None else hash(self.actionCommand))
        result = prime * result + (0 if self.text is None else hash(self.text))
        return result
    
    def __eq__(self, __value: object) -> bool:
        if(isinstance(__value, Option)):
            if(self.text == __value.text and self.actionCommand == __value.actionCommand):
                return True
            else:
                return False
        else:
            return False
    
    def __str__(self) -> str:
        return (str(self.text))