from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
    }

loopback666 = {"id":"666","ip":"66.66.66.66/32"}

ip_add = f"""
<config>
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <ipv4-items>
          <inst-items>
            <dom-items>
              <Dom-list>
                <name>default</name>
                <if-items>
                  <If-list>
                   <id>lo{loopback666["id"]}</id>
                    <addr-items>
                      <Addr-list>
                        <addr>{loopback666["ip"]}</addr>
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
lm = manager.connect(**local_nexus)

netconf_response = lm.edit_config(target="running",config=ip_add)
print(netconf_response)
