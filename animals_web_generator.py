import data_fetcher  # Import the data fetcher module


def generate_website(animal_name, animals_data):
    """
    Creates an HTML file based on the animal data.
    """
    with open("animals.html", "w") as file:
        file.write(f"<h1>Animals: {animal_name}</h1>")

        if animals_data:  # If animals were found
            for animal in animals_data:
                file.write(f"<p>{animal['name']} - </p>")
        else:
            file.write(f"<h2>The animal '{animal_name}' doesn't exist.</h2>")

    print("Website was successfully generated to the file animals.html.")


# Main program
if __name__ == "__main__":
    animal_name = input("Please enter an animal: ")
    data = data_fetcher.fetch_data(animal_name)  # Fetch the data
    generate_website(animal_name, data)  # Generate the website