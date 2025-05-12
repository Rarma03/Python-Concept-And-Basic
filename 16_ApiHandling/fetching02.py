# learn to write fetching a litte more better and professional

import requests

def fetch_random_users(page=1, limit=5):
    url = "https://api.freeapi.app/api/v1/public/randomusers"
    headers = {"accept": "application/json"}
    params = {"page": str(page), "limit": str(limit)}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()

        if data.get('success'):
            users = data['data'].get('data', [])
            for user in users:
                print(f"Name: {user.get('name')}")
                print(f"Cell: {user.get('cell')}")
                print("-" * 30)
        else:
            print("API responded with success=False")

    except requests.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    fetch_random_users()