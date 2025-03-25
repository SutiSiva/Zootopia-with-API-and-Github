import requests


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"https://api.api-ninja.com/v1/animals/{animal_name}"
    headers = {"Authorization": f"Bearer {api_key}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return the JSON response as a Python object
    else:
        return None  # Return None if the request was unsuccessful