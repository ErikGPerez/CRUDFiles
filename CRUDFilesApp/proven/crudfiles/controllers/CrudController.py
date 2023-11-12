from proven.crudfiles.views.CrudView import CrudView
from proven.crudfiles.model.CrudModel import CrudModel

class CrudController:
    
    def __init__(self, model: CrudModel):
        self.model = model
        self.view = CrudView(self, self.model)
        self.view.display()
        
    def processRequest(self, action):

        if action == None:
            action = "wrong_action"
        else:
            if action == "exit":
                self.exitApplication()
            if action == "wrong_action":
                print("Wrong option")
        
    def exitApplication(self):
        quit()
