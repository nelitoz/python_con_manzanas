from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}

bgp_prefixes = """
<filter>
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
                      <AdvPrefix-list>
                      </AdvPrefix-list>
                    </prefix-items>
                  </DomAf-list>
                </af-items>
              </Dom-list>
            </dom-items>
          </inst-items>
        </bgp-items>
      </System>
</filter>
"""
lm_nexus = manager.connect(**local_nexus)

netconf_response = lm_nexus.get_config('running', filter=bgp_prefixes)

ordered_dict = xmltodict.parse(netconf_response.xml)
prefixes_data = ordered_dict["rpc-reply"]["data"]["System"]["bgp-items"]["inst-items"]["dom-items"]["Dom-list"]
prefixes = prefixes_data["af-items"]["DomAf-list"]["prefix-items"]["AdvPrefix-list"]

#print (netconf_response.xml)
print (prefixes)
print ("BGP prefixes configured for VRF TENANT_A:")
for prefix in prefixes:
    print (prefix)
    print (prefix["addr"])
    

#print (prefixes)
