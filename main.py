import requests
import json
import openai
import functools

API_KEY = "INSERT YOUR API KEY HERE"


def get_age():
    """
    Prompts the user to enter their age and returns it as an integer.

    Parameters:
        None

    Returns:
        int: The age entered by the user.
    """
    while True:
        try:
            age = int(input("May I have your Age: "))
            if age < 1 or age > 120:
                print("Please enter a valid age.")
            else:
                return age
        except ValueError:
            print("Please enter a valid age.")


def get_gender():
    """
    Asks the user for their gender and returns it as a string.

    Parameters:
        None

    Returns:
        A string representing the user's gender, which can be "male", "female", or "other".
    """
    while True:
        gender = (
            input("May I have your gender (male, female, or other): ").strip().lower()
        )
        if gender in ["male", "female", "other"]:
            return gender
        else:
            print("Please enter a valid gender.")


def get_mood():
    """
    Asks the user for their current mood and returns it as a string.

    Parameters:
        None

    Returns:
        A string representing the user's mood.
    """
    return input("What's your mood today: ").strip()


def get_weather():
    """
    Asks the user for the current weather and returns it as a string.

    Parameters:
        None

    Returns:
        A string representing the weather.
    """
    return input("How's the weather today: ").strip()


def get_genre():
    """
    Asks the user for their preferred music genre and returns it as a string.

    Parameters:
        None

    Returns:
        A string representing the user's prefeered music genre(s).
    """
    return input("Give me your preferred music genre here: ").strip()


def get_artists():
    """
    Asks the user for their favorite artists and returns them as a list of strings.

    Parameters:
        None

    Returns:
        A string representing the user's favorite artist(s).
    """
    artist = input("Please enter one of your favorite artists: ").strip()
    return artist


def main():
    """
    Driver function for the music recommendation system. Collects user input for age, gender, mood, weather, genre,
    and favorite artists, and uses the OpenAI API to generate recommendations for movies, music, and food based on
    the user's input. Prints the recommendations to the console.

    Parameters:
        None

    Returns:
        None
    """
    openai.api_key = API_KEY
    start = "I am a music recommendation system."
    start2 = "I can suggest songs based on your age, gender, mood, today's weather, genre and favorite artists."
    print(start)
    print(start2)

    age = get_age()
    print(" ")
    gender = get_gender()
    print(" ")
    mood = get_mood()
    print(" ")
    weather = get_weather()
    print(" ")
    genre = get_genre()
    print(" ")
    artists = get_artists()
    print(" ")
    prompt = f"Your profile:\n\nAge: {age}\nGender: {gender}\nMood: {mood}\nWeather: {weather}\nGenre: {genre}\nFavorite Artists: {artists}\n"

    # use the openai.Completion.create method to call the OpenAI API and

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=3500,
        n=10,
        stop=None,
        temperature=0.7,
    )

    choices = response.choices
    recommendations = []
    movies = []
    music = []
    food = []
    for choice in choices:
        text = choice.text.strip()
        if text and text not in recommendations:
            recommendations.append(text)
            num_lines = text.count("\n") + 1
            lines = ""
            if num_lines > 1:
                lines = text.split("\n")
            elif num_lines == 1:
                lines = text
            movies.append(
                [line.split(":")[1].strip() for line in lines if "Movie" in line]
            )
            music.append(
                [line.split(":")[1].strip() for line in lines if "Song" in line]
            )
            #             music.append([line.split(":")[1].strip() for line in lines if "Music" in line])
            food.append(
                [line.split(":")[1].strip() for line in lines if "Food" in line]
            )
    final_music = list(filter(None, music))
    final_movie = list(filter(None, movies))
    final_food = list(filter(None, food))

    if final_music:
        print(" ")
        print("===============================================================")
        print(" ")
        print("Here's your song recommendations: ")
        print("")
        flattened_list = functools.reduce(lambda x, y: x + y, final_music)
        print(", ".join(flattened_list))
        print("")
        print("===============================================================")
        print("")

        if final_movie:
            print("")
            print("Would you like to search for movie recommendations?")
            movie_choice = input("Please enter yes or no: ")
            if movie_choice != "no":
                print(" ")
                print("===============================================================")
                print("Here's your movie recommendations: ")
                print("  ")
                flattened_list = functools.reduce(lambda x, y: x + y, final_movie)
                print(", ".join(flattened_list))
                print("===============================================================")
                print("")

        if final_food:
            print("")
            print("Would you like to search for food recommendations?")
            food_choice = input("Please enter yes or no: ")
            if food_choice != "no":
                print(" ")
                print("===============================================================")
                print("Here's your food recommendations: ")
                print("   ")
                flattened_list = functools.reduce(lambda x, y: x + y, final_food)
                print(", ".join(flattened_list))
                print("===============================================================")
                print(" ")
                print("Hope you enjoy the recommendations from me! Have a nice day :-)")
                print(" ")
                print("========================== END ================================")
        else:
            print(" ")
            print("Hope you enjoy the recommendations from me! Have a nice day :-)")
            print(" ")
            print("========================== END ================================")
    else:
        print("")
        print(
            "Sorry, no music recommendations found for your input, rerun the code and try again"
        )
        print("===============================================================")


if __name__ == "__main__":
    main()
