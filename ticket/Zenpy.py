from decouple import config

# Zenpy accepts an API token
creds = {
    'email' : config(EMAIL),
    'token' : config(TOKEN),
    'subdomain': config(SUBDOMAIN)
}


# Or a password
creds = {
    'email' : config(EMAIL),
    'password' : config(PASS),
    'subdomain': config(SUBDOMAIN)
}

# Import the Zenpy Class
from zenpy import Zenpy
import requests

# Default
zenpy_client = Zenpy(**creds)

# Alternatively you can provide your own requests.Session object
zenpy_client = Zenpy(**creds, session=requests.Session())

# If you are providing your own HTTPAdapter object, Zenpy provides defaults via the
# Zenpy.http_adapter_kwargs() method. You can choose to use these defaults like so:
# session = requests.Session()
# session.mount('https://sample5751.zendesk.com/', MyAdapter(**Zenpy.http_adapter_kwargs()))
# zenpy_client = Zenpy(**creds, session=requests.Session())


