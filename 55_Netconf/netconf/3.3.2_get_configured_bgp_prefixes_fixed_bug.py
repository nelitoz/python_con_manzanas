from ncclient import manager
import sys
from lxml import etree
import xmltodict


# create a main() method
def main():
    """
    Main method that collects the BGP prefixes
    """
    filter_prefix = """
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
                                    <AdvPrefix-list/>
                                </prefix-items>
                            </DomAf-list>
                        </af-items>
                    </Dom-list>
                </dom-items>
            </inst-items>
        </bgp-items>
    </System>
"""
    local_nexus = {
    "host":"192.168.22.237",
    "port":"830",
    "username":"nelitoz",
    "password":"nelitoz",
    "hostkey_verify":False
    }
    lm_nexus = manager.connect(**local_nexus)
    netconf_response = lm_nexus.get(("subtree",filter_prefix))

    prefixes = xmltodict.parse(netconf_response.xml, force_list={"AdvPrefix-list"})["rpc-reply"]["data"]["System"]["bgp-items"]["inst-items"]["dom-items"]["Dom-list"]["af-items"]["DomAf-list"]["prefix-items"]["AdvPrefix-list"]
    for prefix in prefixes:
            print(f"{prefix['addr']}")

if __name__ == '__main__':
    sys.exit(main())

