from proven.crudfiles.model.CrudModel import CrudModel
from proven.crudfiles.controllers.CrudController import CrudController

##Init main to run programm
class Main:
    def __init__(self):
        model = CrudModel()
        control = CrudController(model)

main = Main()
    