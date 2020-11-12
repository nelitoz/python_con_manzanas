# ejemplo para explicar:
# modulos, properties, herencias
# ejecutar en la terminal con el interprete

from toolbox import generate_device_name, is_ipv4_address
class Interface:
    #La clase interface, retorna un objeto de tipo diccionario
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.state = "Down"
    @property
    def address(self):
        return self._address
    
    @address.setter
    def address(self, value):
        if not is_ipv4_address(value):
            raise ValueError(f">> {value} is not a valid ipv4 Address")
        self._address = value
    
    def __repr__(self):
        return str(vars(self))

class Device:
    def __init__(self,hostname):
        self.hostname = hostname
        self.motd = None
        self.interface = None
    def show(self, p=None):
        if not p:
            return str(vars(self))
        elif hasattr(self,p):
            return getattr(self,p)
        else:
            return f"no attribute {p} found"
class Router(Device):
    #La clase Router, hereda a la clase Device
    pass

dev_name = generate_device_name("switch","CORE")
sw1 = Router(dev_name)

sw1.show()
sw1.show("interface")
sw1.interface = Interface("eth0","1.1.1.1")
sw1.show()
sw1.show("interface")
sw1.interface
s1.interface.address = "2.2.2.2"
sw1
sw1.show()
sw1.interface.address= "nelitoz.com"

