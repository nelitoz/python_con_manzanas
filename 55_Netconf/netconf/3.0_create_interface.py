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


# IETF Interface Types
IETF_INTERFACE_TYPES = {
        "loopback": "ianaift:softwareLoopback",
        "ethernet": "ianaift:ethernetCsmacd"
    }

# Ask for the Interface Details to Add
new_loopback = {}
new_loopback["name"] = "Loopback" + input("What loopback number to add? ")
new_loopback["desc"] = input("What description to use? ")
new_loopback["type"] = IETF_INTERFACE_TYPES["loopback"]
new_loopback["status"] = "true"
new_loopback["ip_address"] = input("What IP address? ")
new_loopback["mask"] = input("What network mask? ")


# Create an XML configuration template for ietf-interfaces
netconf_interface_template = f"""
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
                <name>{new_loopback["name"]}</name>
                <description>{new_loopback["desc"]}</description>
                <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">
                {new_loopback["type"]}
            </type>
                <enabled>{new_loopback["status"]}</enabled>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                        <address>
                                <ip>{new_loopback["ip_address"]}</ip>
                                <netmask>{new_loopback["mask"]}</netmask>
                        </address>
                </ipv4>
        </interface>
    </interfaces>
</config>"""

print(netconf_interface_template)

rm = manager.connect(**ncs_devnet)

netconf_reply = rm.edit_config(netconf_interface_template, target = "running")

print(netconf_reply.ok)
print ("")
print(netconf_reply.xml)

