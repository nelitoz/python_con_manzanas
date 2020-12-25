#!/usr/bin/env python
# coding: utf-8

from ncclient import manager, xml_
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


# Create an XML body to execute the save operation
save_body = """
<cisco-ia:save-config xmlns:cisco-ia="http://cisco.com/yang/cisco-ia"/>
"""

rm = manager.connect(**ncs_devnet)

element = xml_.to_ele(save_body)
netconf_reply = rm.dispatch(element)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

