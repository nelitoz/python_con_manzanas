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

# create a new instance of Native Interface object
native_Interfaces_object = xe_model.Native.Interface()

# read the interfaces with the help of read function
xe_interfaces = crud.read(provider, native_Interfaces_object)

# print the primary address of the fifth gigabitethernet interface
print (xe_interfaces.gigabitethernet[0].ip.address.primary.address)
