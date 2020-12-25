#!/usr/bin/env python
# coding: utf-8
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


# Ask for the Interface Details to Add
new_loopback = {}
new_loopback["name"] = "Loopback" + input("What loopback number to delete? ")


# Create an XML configuration template for ietf-interfaces
netconf_interface_template = f"""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface operation="delete">
                <name>{new_loopback["name"]}</name>
        </interface>
    </interfaces>
</config>"""

print (netconf_interface_template)

rm = manager.connect(**ncs_devnet)

netconf_reply = rm.edit_config(netconf_interface_template, target = "running")


print (netconf_reply.xml)
print (netconf_reply.ok)

