from proven.crudfiles.views.CrudMenu import CrudMenu
from proven.crudfiles.model.CrudModel import CrudModel
from proven.crudfiles.controllers.CrudController import *

class CrudView:
    def __init__(self, control, model):
        self.control = control
        self.model = model
        self.menu = CrudMenu()
    
    def showInputDialog(self, message):
        print(message)
        return input()
    
    def showMessage(self, message):
        print(message)
        
    def display(self):
        while True:
            self.menu.show()
            action = self.menu.getSelectedOptionActionCommand()
            self.processAction(action)
            
            
    def processAction(self, action):
        if action != None:
            if action:
                self.control.processRequest(action)
    
    def showFriendTable(self, data):
        cont = 0
        for Friend in data:
            print(Friend)
            cont = cont + 1
        print(str(cont) + " Elements found. " + str(len(data)))
        
    def crudForm(self, inputU):
        return inputU