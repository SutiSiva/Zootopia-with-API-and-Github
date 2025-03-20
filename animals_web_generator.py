import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


animals_data = load_data('animals_data.json')

for animal_data in animals_data:
    print(f"Name: {animal_data.get('name', 'N/A')}")
    print(f"Diet: {animal_data.get('characteristics', {}).get('diet', 'N/A')}")
    if 'locations' in animal_data and animal_data['locations']:
        print(f"Location: {animal_data['locations'][0]}")
    print(f"Type: {animal_data.get('type', 'N/A')}")
    print()  # Leerzeile für bessere Lesbarkeit

file_path = 'animals_template.html'

with open(file_path, 'r') as file:
    file_content = file.read()

print(file_content)

output = ''  # define an empty string
for animal_data in animals_data:
    # append information to each string
    output += f"Name: {animal_data['name']}\n"
    output += f"Diet: {animal_data['characteristics']['diet']}\n"

    if 'locations' in animal_data and animal_data['locations']:
        output += f"Location: {animal_data['locations'][0]}\n"
    output += f"Type: {animal_data.get('type', 'N/A')}\n"


print(output)