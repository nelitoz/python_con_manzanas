#ejemplo para explicar __init__, __repr__ y la funcion show
# explicalo sobre el interprete CLI

class Device: 
    def __init__(self, hostname): 
        self.hostname = hostname 
        self.motd = None 
     
    def show(self, p = None): 
        if not p: 
            return str(vars(self)) 
        elif hasattr(self, p): 
            return (getattr(self, p)) 
        else: 
            return f">> no attribute '{p}'"
    def __repr__(self):
        return (str(self.__dict__))

dev1 = Device("R1")
dev2 = Device("R2")
dev2.motd = "Restricted access"
dev2
dev2.show()
dev2.p = "soy P"
dev2.show()
dev2.show("p")
dev2.show("acls")
