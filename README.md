Music Recommendation Generator
===========================
## SI568 Mini Project

Don't know what songs to listen?

Want to have some new songs to start your day?

Wanna more recommendations?

Music Recommendation Generator is a music recommendation system that suggests songs based on the user's age, gender, mood, weather, genre, and favorite artists. It uses OpenAI's GPT-3 to generate recommendations based on user's inputs.

Getting Started
---------------

1. To use the music recommendation generator, you need to have an API key for OpenAI's GPT-3. You can sign up for OpenAI's GPT-3 and get an API key [here](https://beta.openai.com/signup/).

2. You will also need to have Python 3 installed on your computer. Once you have your API key and Python installed, you can clone the repository and install the required packages using the following commands:

```
git clone https://github.com/<username>/<repository>.git
cd <repository>
pip install -r requirements.txt
```
or
3. You can download the code from Github and unzip it.

Usage
-----

1. To use the music recommendation generator, run the `main.py` file in your terminal using the following command:

```
python main.py
```
or
2. You can run the code on your own code editor.

The program will ask for your age, gender, mood, weather, genre, and favorite artists. Once you have provided the input, the system will generate recommendations for songs, movies, and food based on your profile and choices.

To technical members
--------------------
#### Dependencies

-   `openai` - Python package for accessing the OpenAI API
-   `python-dotenv` - Python package for loading environment variables from a `.env` file

Make sure these packages are installed in the environment where the code will be run.

#### Environment Variables

This project relies on the OpenAI API, which requires an API key. The API key is loaded from an environment variable called `OPENAI_API_KEY`. To run the code, make sure this environment variable is set to a valid OpenAI API key.

#### Code Flow

* The `get_age()`, `get_gender()`, `get_mood()`, `get_weather()`, `get_genre()`, and `get_artists()` functions are all helper functions used by `main()` to prompt the user for information.

* The code uses the OpenAI API to generate recommendations based on the user's profile. The response from the API is processed and the recommendations are printed to the console.

#### Modifying the Code

* To modify the code, make changes to the `main()` function and its helper functions as needed. Be sure to test any changes thoroughly to ensure that they do not introduce any bugs.

* To modify the OpenAI API parameters, such as the model used or the number of recommendations generated, modify the `response` variable in the `main()` function.
