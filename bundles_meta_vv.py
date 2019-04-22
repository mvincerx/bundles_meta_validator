from urllib.request import urlopen
import json
import urllib3
import certifi
from pprint import pprint

def bundles_meta_vv():
    """
    Validates bundles' metadata by checking if titles, descriptions, and tags are empty and reports results.
    """
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',ca_certs=certifi.where())
    req = http.request('GET', "https://download.clearlinux.org/releases/current/assets/bundles/bundles.json",  timeout=10.0)
    json_data = json.loads(req.data.decode('utf-8'))
    bundles = json_data["bundles"]
    title = [value for d in bundles for key, value in d.items() if any(d["title"])==False] or print("Titles OK")
    desc =  [value for d in bundles for key, value in d.items() if any(d["description"])==False] or print("Descriptions OK")
    tags =  [value for d in bundles for key, value in d.items() if any(d["tags"])==False] or print("Tags OK")
    clean = [s for s in [title,desc,tags] if s is not None]
    result =  pprint(f"Data missing: {clean[0][::5]}", width=1)
    return result

bundles_meta_vv()
