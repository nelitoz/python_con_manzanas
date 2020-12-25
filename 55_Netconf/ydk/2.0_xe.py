from ydk.models.cisco_ios_xe import Cisco_IOS_XE_native as xe_model

from ydk.services import CRUDService
from ydk.providers import NetconfServiceProvider

# CSR1kv1 Credentials
csr_data = {
        "address":"192.168.22.228",
        "port":830,
        "username":"nelitoz",
        "password":"nelitoz",
        "protocol":"ssh"
        }

# create a PROVIDER
provider = NetconfServiceProvider(**csr_data)
# create a CRUD service
crud = CRUDService()

#get hold of only the first GigabitEthernet interface without the other interfaces
xe_int_giga = xe_model.Native.Interface.GigabitEthernet()
xe_int_giga.name = "1"

# read the interfaces with the help of read function
interface_data = crud.read(provider, xe_int_giga)

# print the primary address of the interface
print (interface_data.ip.address.primary.address)

xe_int_giga.description = "YDK Netconfig created description"
crud.update(provider, xe_int_giga)
interface_data = crud.read(provider, xe_int_giga)
print (interface_data.description)
