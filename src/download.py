import os
import json
import requests
from datetime import datetime, timezone
from pathlib import Path
from pprint import pprint
from dotenv import load_dotenv
import re

def slugify(string):
    # Convert to lowercase
    text = string.lower()
    # Replace any non-alphanumeric character with a hyphen
    text = re.sub(r'[^a-z0-9]+', '-', text)
    # Remove repeated hyphens
    text = re.sub(r'-+', '-', text)
    # Remove leading or trailing hyphens
    return text.strip('-')

# Load environment variables from .env file
load_dotenv()

HOST = os.getenv('HOST')
TOKEN = os.getenv('TOKEN')

response = requests.get(f"{HOST}/v1/stacks", headers={
    'Authorization': f"Bearer {TOKEN}",
    'Content-Type': 'application/json'
})

enabled_journeys = [
    (
        journey["uuid"],
        slugify(journey["name"])
    )
    for journey
    in response.json()
    if journey["enabled"]
]

for (uuid, file_name) in enabled_journeys:
    response = requests.get(f"{HOST}/v1/stacks/{uuid}", headers={
        'Authorization': f"Bearer {TOKEN}",
        'Content-Type': 'application/json'
    })
    data = response.json()
    with open(Path("journeys") / f"{file_name}.json", 'w') as f:
        json.dump(data, f, indent=2)
