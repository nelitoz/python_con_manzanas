from ncclient import manager

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}

bgp_prefixes = """
<config>
<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <bgp-items>
          <inst-items>
            <asn>65001</asn>
            <dom-items>
              <Dom-list>
                <name>TENANT_A</name>
                <af-items>
                  <DomAf-list>
                    <type>ipv4-ucast</type>
                    <prefix-items>
                      <AdvPrefix-list operation="remove">
                      <addr>66.66.66.66/32</addr>
                      </AdvPrefix-list>
                    </prefix-items>
                  </DomAf-list>
                </af-items>
              </Dom-list>
            </dom-items>
          </inst-items>
        </bgp-items>
      </System>
</config>
"""
lm_nexus = manager.connect(**local_nexus)

nc_response = lm_nexus.edit_config(target="running", config=bgp_prefixes)

print (nc_response)
