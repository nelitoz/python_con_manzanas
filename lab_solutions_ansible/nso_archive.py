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

# use archive.xml to configure csr1 using nso
api_endpoint = f'{API_BASE}/api/running/devices/device/csr1/config'
with open('archive.xml') as xml:
    api_response = api_session.patch(api_endpoint, headers=API_HEAD, data=xml)
print(f'-> PATCH: {api_endpoint}')
print(f'  -> RESPONSE: {api_response.status_code}')