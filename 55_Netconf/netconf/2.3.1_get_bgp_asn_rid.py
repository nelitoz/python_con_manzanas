from ncclient import manager
import xmltodict

local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
}

bgp_data = """
<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
        <bgp-items>
          <inst-items>
            <asn/>
            <dom-items>
              <Dom-list>
                <rtrId/>
                <name>default</name>
              </Dom-list>
            </dom-items>
          </inst-items>
        </bgp-items>
      </System>
"""
lm_nexus = manager.connect(**local_nexus)
netconf_response = lm_nexus.get(("subtree",bgp_data))

print (f"This is the complete response,\n{netconf_response}")

netconf_ordered_dict = xmltodict.parse(netconf_response.xml)
bgp_nc_data = netconf_ordered_dict["rpc-reply"]["data"]["System"]["bgp-items"]["inst-items"]
print (f"BGP AS: {bgp_nc_data['asn']} with RID: {bgp_nc_data['dom-items']['Dom-list']['rtrId']}")
