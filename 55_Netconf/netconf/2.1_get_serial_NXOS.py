"""
Objetives:
    1. Use a YANG Module information to create a request for the serial number of the nexus device.
    2. Print the result to user
"""
from ncclient import manager
import xmltodict

rm_device = {
        "host":"sbx-nxos-mgmt.cisco.com",
        "port":"10000",
        "username":"admin",
        "password":"Admin_1234!",
        "hostkey_verify":False
        }
lm_device = {
        "host":"192.168.22.237",
        "port":"830",
        "username":"admin", 
        "password":"cisco123", 
        "hostkey_verify":False
        }
 
#Creamos el filtro de Serial

#Sacamos el namespace de las capacidades extraidas en el proceso hello
#Sacamos los tags con la salida del pyang del modulo YANG que nos interesa

filter_serial = """
  <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
   <serial>
   </serial>
  </System>
  """
lm = manager.connect(**lm_device)
netconf_reply = lm.get(("subtree", filter_serial))

xml_data_to_dict = xmltodict.parse(netconf_reply.xml)["rpc-reply"]["data"]
serial = xml_data_to_dict["System"]["serial"]

print (f"Complete XML response:\n{netconf_reply.xml}")

print (f"Data section from XML:\n{xml_data_to_dict}")
print ("")
print (f"Serial Number is:{serial}")
#print (netconf_reply.xml)

