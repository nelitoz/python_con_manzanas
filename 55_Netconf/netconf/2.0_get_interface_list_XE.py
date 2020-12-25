from ncclient import manager
import xmltodict
import xml.dom.minidom

ncs_local = {
    "host":"192.168.22.59",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}
ncs_devnet = {
    "host":"ios-xe-mgmt.cisco.com",
    "port":"10000",
    "username":"developer",
    "password":"C1sco12345",
    "hostkey_verify":False
}

int_filter = """
<filter>
 <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
  <interface></interface>
 </interfaces>
</filter>
"""

#lm = manager.connect(**ncs_local)
rm = manager.connect(**ncs_devnet)

rm_response = rm.get_config(source= "running", filter=int_filter)

# xml.dom.minidom.parseString ==> Return a Document that represents the string
#lm_xml_object_parsed = xml.dom.minidom.parseString(lm_response.xml)
#print (lm_xml_object_parsed.toprettyxml())

rm_xml_object_parsed = xml.dom.minidom.parseString(rm_response.xml)
# print (rm_xml_object_parsed.toprettyxml)


# xmltodict.parse ==> return an ordered dictionary
#lm_ordered_dict_from_xml = xmltodict.parse(lm_response.xml)
rm_ordered_dict_from_xml = xmltodict.parse(rm_response.xml)


#lm_netconf_data =  (lm_ordered_dict_from_xml['rpc-reply']['data'])
rm_netconf_data =  (rm_ordered_dict_from_xml['rpc-reply']['data'])


#lm_interfaces = lm_netconf_data["interfaces"]["interface"]
rm_interfaces = rm_netconf_data["interfaces"]["interface"]


for interface in rm_interfaces:
    print (f"Interface {interface['name']}, Enabled: {interface['enabled']}")


for interface in rm_interfaces:
    if interface['enabled'] == "true":
        print (interface["name"])


#lm.close_session()
rm.close_session()


