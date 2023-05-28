import requests
import yaml

# URL of the YAML file on GitHub
yaml_url = "https://raw.githubusercontent.com/frk1/hazedumper/master/csgo.yaml"

# Make a GET request to fetch the YAML content
response = requests.get(yaml_url)

class DotDict(dict):
    def __getattr__(self, key):  # Corrected method name
        try:
            return self[key]
        except KeyError:
            raise AttributeError(f"'DotDict' object has no attribute '{key}'")

# Check if the request was successful
if response.status_code == 200:
    # Parse the YAML content as a dictionary
    data = yaml.safe_load(response.text)
    #print(data.get("signatures").get("m_iCrosshairId"))
    Offsets = DotDict(**data.get("netvars"),**(data.get("signatures")))
    print(Offsets.m_zoomLevel)
else:
    print("Failed to fetch YAML file from GitHub.")


