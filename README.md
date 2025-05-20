# Gladly
Gladly Assignment

This project is a CLI tool that integrates with the Gladly API to fetch and import conversation data into Enterpret. It supports incremental imports to avoid duplicating previously fetched data.

Features
Connects to the Gladly API and fetches conversation records.

Supports incremental imports using the updated_at timestamp.

Stores last successful sync time locally to resume from where it left off.

CLI runnable with minimal setup.

Tech Stack
Language: Python 3 (can be ported to Go if required)

Libraries: requests, json, datetime

Understanding Gladly
Gladly is a customer service platform that manages conversations across various channels. Their API provides access to:

Conversations

Messages

Customer profiles

Timestamps for filtering updates

For this integration, we use the conversations endpoint to fetch updated conversations since the last import.

API Base URL: https://api.gladly.com/
Authentication: Bearer Token (Authorization: Bearer <token>)

📂 Project Structure
bash
Copy
Edit
gladly_importer/
├── main.py                 # CLI runner
├── gladly_client.py        # API interaction logic
├── store.py                # Timestamp persistence
├── config.py               # Config settings (API key, base URL)
├── last_import.json        # Stores the last successful import time
├── requirements.txt        # Python dependencies
└── README.md               # This file
Incremental Import Logic
On every run, the tool reads the last_import.json file to determine the last successful import time.

It fetches all conversations updated after this timestamp using Gladly’s updated_since query parameter (or equivalent).

It stores the new latest_updated_at from the fetched data for the next run.

Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/gladly-importer.git
cd gladly-importer
2. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3. Configure API Key
Create a file named config.py:

python
Copy
Edit
API_TOKEN = "your_gladly_api_token"
BASE_URL = "https://api.gladly.com"
4. Run the CLI
bash
Copy
Edit
python main.py
