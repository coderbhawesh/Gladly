import requests

API_URL = "https://api.gladly.com//api/v1/agents" 
TOKEN = "your_token"

def fetch_conversations(since_timestamp):
    headers = {"Authorization": f"Bearer {TOKEN}"}
    params = {"updated_since": since_timestamp}  # Depends on API spec
    all_data = []
    latest_time = since_timestamp

    while True:
        response = requests.get(API_URL, headers=headers, params=params)
        data = response.json()
        conversations = data.get("conversations", [])

        if not conversations:
            break

        all_data.extend(conversations)
        latest_time = max(c['updated_at'] for c in conversations)

        # Handle pagination if needed
        next_url = data.get("next")
        if not next_url:
            break
        API_URL = next_url

    return all_data, latest_time
