from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}
ip_filter = """
<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <ipv4-items>
          <inst-items>
            <dom-items>
              <Dom-list>
                <name>default</name>
                <if-items>
                  <If-list>
                    <id/>
                    <addr-items>
                      <Addr-list>
                        <addr/>
                      </Addr-list>
                    </addr-items>
                  </If-list>
                </if-items>
              </Dom-list>
            </dom-items>
          </inst-items>
        </ipv4-items>
      </System>
"""
loopback_filter = """
<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <intf-items>
          <lb-items/>
        </intf-items>
</System>
"""
lm = manager.connect(**local_nexus)

lm_ip_filter_reply = lm.get(("subtree", ip_filter)).xml
lm_loopbacks_reply = lm.get(("subtree",loopback_filter)).xml

loopback_dict = xmltodict.parse(lm_loopbacks_reply)
loopbacks = loopback_dict['rpc-reply']['data']['System']['intf-items']['lb-items']['LbRtdIf-list']

print ("Tienes las siguientes interfaces loopbacks")
for loopback in loopbacks:
    print (loopback["id"])


interfaces_dict = xmltodict.parse(lm_ip_filter_reply)
interfaces = interfaces_dict['rpc-reply']['data']['System']['ipv4-items']['inst-items']['dom-items']['Dom-list']['if-items']['If-list']

print ("")

for interface in interfaces:
    if interface["id"][:2]=="lo":
        print (f"La interface {interface['id']}, tienen la IP: {interface['addr-items']['Addr-list']['addr']}")
