import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file
API_KEY = os.getenv('API_KEY')  # Get the API key from the environment variable


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary.
    """
    url = f"https://api.api-ninja.com/v1/animals/{animal_name}"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return the JSON response as a Python object
    else:
        return None  # Return None if the request was unsuccessful