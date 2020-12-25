from ncclient import manager

m = manager.connect(
        host = "192.168.22.59",
        port = 830,
        username = "nelitoz",
        password = "nelitoz",
        hostkey_verify = False
        )

for capability in m.server_capabilities:
    print (capability)

m.close_session()

