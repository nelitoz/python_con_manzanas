from ncclient import manager


def main():
    # Main function to get Netconf capabilities from a nexus device
    rm_data = {
        "host":"sbx-nxos-mgmt.cisco.com",
        "port":"10000",
        "username":"admin", 
        "password":"Admin_1234!", 
        "hostkey_verify":False
        }
    lm_data = {
        "host":"sbx-nxos-mgmt.cisco.com",
        "port":"10000",
        "username":"admin", 
        "password":"Admin_1234!", 
        "hostkey_verify":False
        }
 
    lm = manager.connect(**lm_data)
    
    for capability in lm.server_capabilities:
        print (capability)

if __name__ == "__main__":
    main()

    
