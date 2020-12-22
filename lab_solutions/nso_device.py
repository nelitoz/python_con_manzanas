import requests

# credentials
API_USER = 'admin'
API_PASS = 'admin'
# nso server address
API_BASE = 'http://nso:8080'
# api headers
API_HEAD = {
    'Accept': 'application/vnd.yang.data+xml'
}

api_session = requests.Session()
api_session.auth = (API_USER, API_PASS)

# create nso device from csr1.xml
api_endpoint = f'{API_BASE}/api/running/devices/device/csr1'
with open('csr1.xml') as xml:
    api_response = api_session.put(api_endpoint, headers=API_HEAD, data=xml)
print(f'-> PUT: {api_endpoint}')
print(f'  -> RESPONSE: {api_response.status_code}')

# tell nso to fetch ssh keys
api_endpoint = f'{API_BASE}/api/running/devices/device/csr1/ssh/_operations/fetch-host-keys'
api_response = api_session.post(api_endpoint, headers=API_HEAD)
print(f'-> POST: {api_endpoint}')
print(f'  -> RESPONSE: {api_response.status_code}')

# tell nso to sync configuration from device
api_endpoint = f'{API_BASE}/api/running/devices/device/csr1/_operations/sync-from'
api_response = api_session.post(api_endpoint, headers=API_HEAD)
print(f'-> POST: {api_endpoint}')
print(f'  -> RESPONSE: {api_response.status_code}')



