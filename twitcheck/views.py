from django.shortcuts import render
import requests
import os
from dotenv import load_dotenv

from .forms import TwitchForm

def check_twitch_live(request):
    if request.method== 'POST':
        form=TwitchForm(request.POST)
        if form.is_valid():
            load_dotenv()
            try:
                client_id = os.getenv('CLIENT_ID')
                client_secret = os.getenv('CLIENT_SECRET')
                streamer_name = form.cleaned_data['username']

                body = {
                    'client_id': client_id,
                    'client_secret': client_secret,
                    "grant_type": 'client_credentials'
                }
                r = requests.post('https://id.twitch.tv/oauth2/token', body)

                #data output
                keys = r.json()

                headers = {
                    'Client-ID': client_id,
                    'Authorization': 'Bearer ' + keys['access_token']
                }

                stream = requests.get('https://api.twitch.tv/helix/streams?user_login=' + streamer_name, headers=headers)

                stream_data = stream.json()

                if len(stream_data['data']) == 1:
                    stream_title=str(stream_data['data'][0]['title'])
                    stream_game=str(stream_data['data'][0]['game_name'])
                    return render(request, 'results.html', {'stream_title':stream_title, 'streamer_name':streamer_name, 'stream_game':stream_game})
                else:   
                    info=str(streamer_name + ' is not live')
                    return render(request, 'results.html', {'not_live':info})
            except KeyError:
                error_message = f"Channel '{streamer_name}' not found."
                return render(request, 'error.html', {'message': error_message})
        else:
            error_message = f"An unkown error occured, please try again!"
            return render(request, 'error.html', {'message': error_message})
    else:
        form = TwitchForm()
    return render(request, 'check_twitch.html', {'form':form})