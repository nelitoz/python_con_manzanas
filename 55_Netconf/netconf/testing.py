from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
    }

message = """
         <source xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
             <running/>
         </source>
"""

nc_nexus = manager.connect(**local_nexus)

print (nc_nexus.connected)
nc_response = nc_nexus.get_config(source="running")

print (nc_response)
