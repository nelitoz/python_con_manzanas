from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}
prefix = {"as":"65001","vrf":"TENANT_A", "af":"ipv4-ucast","prefix":"66.66.66.66/32"}

advertise_prefix = f"""
    <config>
      <System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <bgp-items>
          <inst-items>
            <asn>{prefix["as"]}</asn>
            <dom-items>
              <Dom-list>
                <name>{prefix["vrf"]}</name>
                <af-items>
                  <DomAf-list>
                    <type>{prefix["af"]}</type>
                    <prefix-items>
                      <AdvPrefix-list>
                        <addr>{prefix["prefix"]}</addr>
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

netconf_response = lm_nexus.edit_config(target="running",config=advertise_prefix)

print(netconf_response)
