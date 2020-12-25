from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}
loopback = {"id": "666", "ip": "66.66.66.66/32"}
lm = manager.connect(**local_nexus)

configuration = f"""
    <config>
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <intf-items>
          <lb-items>
            <LbRtdIf-list>
              <id>lo{loopback["id"]}</id>
            </LbRtdIf-list>
          </lb-items>
        </intf-items>
        <ipv4-items>
          <inst-items>
            <dom-items>
              <Dom-list>
                <name>default</name>
                <if-items>
                  <If-list>
                    <id>lo{loopback["id"]}</id>
                    <addr-items>
                      <Addr-list>
                        <addr>{loopback["ip"]}</addr>
                      </Addr-list>
                    </addr-items>
                  </If-list>
                </if-items>
              </Dom-list>
            </dom-items>
          </inst-items>
        </ipv4-items>
      </System>
    </config>
"""

netconf_reply = lm.edit_config(target="running", config=configuration)

print (netconf_reply)

