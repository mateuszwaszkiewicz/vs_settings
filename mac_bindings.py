import json

# Remove illegal trailing commas before parsing
import re

import requests

# Download the keybindings.json file
url = "https://raw.githubusercontent.com/mateuszwaszkiewicz/vs_settings/main/keybindings.json"
response = requests.get(url)
raw_json = response.text

# Remove trailing commas before closing braces/brackets
clean_json = re.sub(r",(\s*[}\]])", r"\1", raw_json)

keybindings = json.loads(clean_json)

# Replace "ctrl" with "cmd" in the "key" field
for binding in keybindings:
    if "key" in binding and "ctrl" in binding["key"]:
        binding["key"] = binding["key"].replace("ctrl", "cmd")

# Save the modified keybindings to a new file
with open("mac_keybindings.json", "w") as f:
    json.dump(keybindings, f, indent=4)
