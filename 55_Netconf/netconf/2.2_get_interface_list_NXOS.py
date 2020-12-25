from ncclient import manager

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}

filter = """
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
lm = manager.connect(**local_nexus)

lm_reply = lm.get(("subtree", filter))

print (lm_reply.xml)
