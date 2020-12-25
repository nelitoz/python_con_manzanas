from ncclient import manager
import xmltodict

local_nexus = {
        "host":"192.168.22.237",
        "port":"830",
        "username":"nelitoz",
        "password":"nelitoz",
        "hostkey_verify":False
        }
nc_connection = manager.connect(**local_nexus)

add_oc_interface = f"""
 <config>
 <interfaces xmlns="http://openconfig.net/yang/interfaces">
     <interface>
         <name>lo777</name>
         <config>
             <description> Configured using OpenConfig Model </description>
             <name>lo777</name>
             <type>ianaift:softwareLoopback</type>
         </config>
         <subinterfaces>
             <subinterface>
                 <index>0</index>
                 <ipv4>
                     <addresses>
                         <address>
                             <config>
                                 <ip>77.77.77.77</ip>
                                 <prefix-length>24</prefix-length>
                             </config>
                             <ip>77.77.77.77</ip>
                         </address>
                     </addresses>
                 </ipv4>
             </subinterface>
         </subinterfaces>
     </interface>
 </interfaces>
 </config>"""


nc_response = nc_connection.edit_config(target="running",config=add_oc_interface)

print (nc_response)
