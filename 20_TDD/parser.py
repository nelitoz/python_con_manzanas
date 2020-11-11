import re
class ConfigurationParser:
    fhand = open("router.txt","r")
    deviceConfig = fhand.read()
    fhand.close()
    def parseCustomerNames(self):
        customerNamePattern = r"ip vrf ([a-zA-Z_]+)\n"
        customerNames = re.findall(customerNamePattern,self.deviceConfig)
        return customerNames
    def parseCustomerVlans(self, customer):
        vlanPattern = (
                      r"interface GigabitEthernet0\/0\.([0-9]+)\n  encapsulation "
                      r"dot1Q [0-9]+\n  ip vrf forwarding %s"
                      %(customer)
                      )
        vlanID = re.findall(vlanPattern, self.deviceConfig)
        return vlanID
    def parseCustomerIP(self, vlan):
        #IPPattern = r"^GigabitEthernet0/0\.%s +(.*)" %(vlan)
        IPPattern = r'GigabitEthernet0\/0\.%s +(.*)'% (vlan)
        IP = re.search(IPPattern, self.deviceConfig)
        return IP.group(1)
    def parseCustomerData(self):
        diccionario ={}
        for customer in self.parseCustomerNames():
            vlan_list = self.parseCustomerVlans(customer)
            for vlan in vlan_list:
                vlan = int(vlan)
                ip = self.parseCustomerIP(vlan)
                if customer in diccionario:
                    diccionario[customer].append([vlan, ip])
                else:
                    diccionario[customer] =[[vlan,ip]]
        return diccionario

