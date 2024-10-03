# Hubeta

This repository contains the FLOIP specification that runs the Hubeta WHAtsApp service on Turn.io.
It also contains the scripts necessary to fetch and update the journeys used in the service.

This script, `download.py`, is designed to fetch and save enabled journeys from a backend API. The API endpoint and credentials are loaded from a `.env` file using the `dotenv` package.

# Structure

This script assumes a specific directory structure:

* The `.env` file containing API credentials should be placed in the same directory as the script.
* The `journeys/` directory store the JSON FLOIP specifications for the conversational flows
* THe `src/` directory stores the scripts necessary to fetch the journey data from Turn


# Download the Journeys

To use this script:

1. Create a `.env` file containing your API credentials in the same directory as the script.
1. Install the required Python packages by running `pip install -r requirements.txt` in your terminal.
1. Run the script with `python src/download.py`.

The script will fetch enabled journeys from the Turn.io API, create a JSON file for each journey
named after its slugified name, and save it in a `journeys/` directory.
