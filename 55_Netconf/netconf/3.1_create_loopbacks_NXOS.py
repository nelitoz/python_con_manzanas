from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}

loopback_666 = {"id":"666","ip":"66.66.66.66/24"}
add_loopback = f"""
<config>
<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
      <intf-items>
        <lb-items>
          <LbRtdIf-list>
            <id>lo{loopback_666['id']}</id>
            <adminSt>up</adminSt>
            <descr>Interface Padroteada por NETCONF</descr>
          </LbRtdIf-list>
        </lb-items>
      </intf-items>
</System>
</config>
"""
lm = manager.connect(**local_nexus)
print ("Local Manager connected")
netconf_response = lm.edit_config(target="running", config=add_loopback)

print("good")
print (netconf_response)
