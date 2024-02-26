
# Twitcheck (Twitch Live Check Application)

# Overview 
This Django app allows users to input a line of text through a form, and it checks if there is a corresponding Twitch streamer who is currently live. The app utilizes the Twitch API to fetch live stream information based on the provided input.

# Features

Form Input: Users can enter a line of text (Twitch username) in the provided form.

Twitch API Integration: The app communicates with the Twitch API to check if there is a live stream corresponding to the input.

Live Status Display: The app displays whether the Twitch streamer is currently live or not.

Detailed Information: Users can view additional details about the live stream, such as the stream title, number of viewers, and more.
# Requirements
Make sure you have the following installed:

Python (3.6 or higher)\
Django (3.2 or higher)\
Requests library (for making API calls)

# Configuration
Make sure to set up your Twitch API credentials in the settings.py file:
settings.py

CLIENT_ID = 'your_twitch_client_id'\
CLIENT_SECRET = 'your_twitch_client_secret'

You can obtain your Twitch API credentials by creating a new application on the Twitch Developer Portal.

# Usage
Enter a Twitch.tv username in the form and submit. \
The app will display whether the corresponding Twitch streamer is currently live or not. \
Additional details about the live stream will be shown on the page if the streamer is live. \
Feel free to customize and extend the app according to your requirements!

