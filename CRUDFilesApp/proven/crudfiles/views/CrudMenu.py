from proven.crudfiles.views.Option import Option
from proven.crudfiles.views.Menu import Menu


class CrudMenu(Menu):
    
    def __init__(self):
        super().__init__("Crud Manager main menu")
        self.addOption(Option("Exit", "exit"))
        