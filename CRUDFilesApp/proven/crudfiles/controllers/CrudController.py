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
            if action == "crear_fitxer":
                self.crearFitxer()
            if action == "llegir_fitxer":
                self.llegirFitxer()
            if action == "escriure_fitxer":
                self.escriureFitxer()
            if action == "esborrar_fitxer":
                self.esborrarFitxer()
            if action == "wrong_action":
                print("Wrong option")
    
    def exitApplication(self):
        quit()
        
    def crearFitxer(self):
        filepath = self.view.showInputDialog("Nom del nou arxiu: ")
        if self.model.createFile(filepath):
            self.view.showMessage("L'arxiu " + filepath + " s'ha creat correctament")
        else:
            self.view.showMessage("L'arxiu " + filepath + " no s'ha creat")
            
    def llegirFitxer(self):
        filepath = self.view.showInputDialog("Nom del arxiu a llegir: ")
        fileRead = self.model.readFile(filepath)
        if fileRead != "":
            self.view.showMessage("Arxiu " + filepath)
            self.view.showMessage(fileRead)
        else:
            self.view.showMessage("Arxiu vuit o no s'ha trobat")
    
    def escriureFitxer(self):
        filepath = self.view.showInputDialog("Nom del arxiu per escriure: ")
        text: str = self.view.showInputDialog("Quin missatge vols posar?: ")
        done = self.model.writeFile(filepath, text)
        if done == False:
            self.view.showMessage("No s'ha pogut fer l'operació")
        
    def esborrarFitxer(self):
        filepath = self.view.showInputDialog("Nom del arxiu per esborrar: ")
        if self.model.removeFile(filepath):
            self.view.showMessage("L'arxiu " + filepath + " s'ha esborrat correctament")
        else:
            self.view.showMessage("L'arxiu " + filepath + " no s'ha esborrat")