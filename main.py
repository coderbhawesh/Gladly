from gladly_client import fetch_conversations
from store import get_last_import_time, save_last_import_time

def main():
    last_time = get_last_import_time()
    conversations, latest_time = fetch_conversations(last_time)
    # You can process/store conversations here (e.g., to DB or JSON file)
    save_last_import_time(latest_time)

if __name__ == "__main__":
    main()
