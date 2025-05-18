import requests
import json
import os 


def fetch_eia_data():
    api_key = os.getenv("EIA_API_KEY")
    if not api_key:
        raise EnvironmentError("❌ EIA_API_KEY not found in environment variables.")
    series_id = "PET.RWTC.D"
    url = f"https://api.eia.gov/v2/seriesid/{series_id}?api_key={api_key}"
    
    response = requests.get(url)

    if response.status_code != 200:
        print(f"❌ HTTP error: {response.status_code}")
        print(response.text)
        raise Exception("❌ Failed to fetch EIA data due to HTTP error")

    data = response.json()

    # Check for known API error structures
    if "response" not in data:
        print("❌ API responded with invalid structure:")
        print(json.dumps(data, indent=2))
        raise Exception("❌ EIA API response missing 'response' key")

    # Save data if no issues
    with open("/tmp/raw_eia_data.json", "w") as f:
        json.dump(data, f)

    print("✅ Data saved to /tmp/raw_eia_data.json")


if __name__ == "__main__":
    fetch_eia_data()