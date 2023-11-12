class Menu:
    def __init__(self, title: str):
        self.title = title
        self.options = list()

    def reset(self):
        self.title = None
        self.options = list()

    def getOption(self, index):
        return self.options.get(index)

    def addOption(self, Option) -> bool:
        return self.options.append(Option)

    def removeOption(self, Option):
        return self.options.remove(Option)

    def __str__(self) -> str:
        return ("Title = " + str(self.title) + ", Options = " + str(self.options))

    def show(self):
        print("=============="+self.title+"================")
        idOption = 0
        for Option in self.options:
            print(str(Option) + ": " + str(idOption))
            idOption += 1
        
    def getSelectedOption(self) -> int:
        """Gets the selected option. If fails, resturns -1

        Returns:
            int: Option choosen. If not, -1
        """
        opt = -1
        try:
            print("Select an Option: ")
            opt = int(input())
            if opt < 0 or opt >= len(self.options):
                opt = -1
        except :
            opt = -1
        return opt
    
    def getSelectedOptionActionCommand(self):
        optionNumber = self.getSelectedOption()
        actionCommand = None
        if optionNumber >= 0 and optionNumber < len(self.options):
            actionCommand = self.options[optionNumber].actionCommand
        else:
            actionCommand = "wrong_action"
        return actionCommand