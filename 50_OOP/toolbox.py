def generate_device_name(device, description):
    datacenter = "QRO"
    devices = {"firewall":"ASAv","router":"6500","switch":"N9k"}

    device_type = devices[device]
    device_name = f"{device_type}--{description}__{datacenter}"
    #device_type--description__dataCenter
    return (device_name)

#name = generate_device_name("switch","CORE")
#print (name)

def is_ipv4_address(ip):
    octects = ip.split(".")
    if len(octects) != 4:
        return False
    elif any(not octect.isdigit() for octect in octects):
        return False
    elif any(int(octect) < 0 for octect in octects):
        return False
    elif any(int(octect)>255 for octect in octects):
        return False
    return True

#is_ip = is_ipv4_address("192.168.22.15")
#print (is_ip)
#is_ip = is_ipv4_address("192.168.322.15")
#print (is_ip)
