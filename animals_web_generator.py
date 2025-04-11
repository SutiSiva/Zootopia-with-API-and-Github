import data_fetcher  # Import the data fetcher module


def generate_website(animal_name, animals_data):
    """
    Creates an HTML file based on the animal data.
    """
 # with open("animals.html", "w") as file:
 #     file.write(f"<h1>Animals: {animal_name}</h1>")
 #
 #       if animals_data:  # If animals were found
 #           for animal in animals_data:
 #               file.write(f"<p>{animal['name']} - </p>")
 #       else:
 #           file.write(f"<h2>The animal '{animal_name}' doesn't exist.</h2>")
 #
 #   print("Website was successfully generated to the file animals.html.")

    #1 Animals Templates Html Datei einlesen
    with open("animals_template.html", "r") as file:
        contents = file.read()

    #2 platzhalter string ersetzen durch gefundene Tiere /API output
    #dict, leer , none
    html_content = ""
    if animals_data is None:
        html_content = f"<h2> error fetching API for Animal '{animal_name}' .</h2>"
    else:
        if animals_data:  # If animals were found
            for animal in animals_data:
                html_content += '<li class="cards__item">\n'
                html_content += f'<div class="card__title">{animal["name"]}</div>\n'
                html_content += '<p class="card__text">\n'
                html_content += f'<strong>Diet:</strong> {animal["characteristics"].get("diet", "N/A")}<br/>\n'
                html_content += f'<strong>Location:</strong> {", ".join(animal["locations"])}<br/>\n'
                html_content += f'<strong>Type:</strong> {animal["characteristics"].get("type", "N/A")}<br/>\n'
                html_content += '</p></li>\n'
        else:
            html_content = f"<h2>The animal '{animal_name}' doesn't exist.</h2>"

    modified_contents = contents.replace("__REPLACE_ANIMALS_INFO__", html_content)

    #3 neuen html code in animals.html speichern
    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(modified_contents)
# Main program
if __name__ == "__main__":
    animal_name = input("Please enter an animal: ")
    data = data_fetcher.fetch_data(animal_name)  # Fetch the data
    generate_website(animal_name, data)  # Generate the website