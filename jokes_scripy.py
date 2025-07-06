import pyjokes
from pick import pick
from pathlib import Path
import requests


language_map = {
    "German": "de",
    "English": "en",
    "Spanish": "es",
    "Italian": "it",
    "French": "fr",
    "Russian": "ru",
    "Swedish": "sv",
    }


def get_chuck_norris_jokes():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    print(response.json()["value"])



def get_number_of_jokes():
    default_number=10
    number= input("Please enter number of jokes")
    if not number.isnumeric():
        print (f"Invalid Input, using default value of {default_number}.")
        return int(default_number)
    return int(number)


def get_language():
    title = "Please choose language:"
    options = ["German", "English", "Spanish", "Italian", "French", "Russian", "Swedish"]
    option, _ = pick(options, title)
    return option


def get_language_code(language_name):
    return language_map.get(language_name)


def get_joke_categories():
    options = {
        "neutral": "Standard programmer jokes",
        "chuck":   "Chuck Norris programmer jokes",
        "all":     "All joke categories combined"
    } 
    print("Please choose a joke category:")
    for key, description in options.items():
        print(f"{key}- {description}")
    category = input().lower().strip()
    if category not in options:
        print("Invalid choice, end program.")
        return
    return category
    
def write_jokes_into_file(language_code, category, joke_count):
    path = Path("jokes.txt")
    mode = "w"  
    if path.is_file():
        print("File already exists. Would you like to overwrite the existing content, default is yes")
        answer = input("Do you want to overwrite it? (Yes/No) [default: Yes]: ").lower().strip()
        if answer == "no":
            mode = "a"  
    seen_jokes = set()
    with open(path, mode) as f:
        for _ in range(joke_count):
            joke = pyjokes.get_joke(language_code, category)
            if joke not in seen_jokes:
                seen_jokes.add(joke)
                f.write(joke + "\n")



def main():
    get_chuck_norris_jokes()
    joke_count = get_number_of_jokes()
    language = get_language()
    language_code = get_language_code(language)
    category=get_joke_categories()
    write_jokes_into_file(language_code, category, joke_count)


if __name__ == "__main__":
    main()
