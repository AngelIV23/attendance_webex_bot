import requests
import os, json
from dotenv import load_dotenv

def load_dotenv_vars():
    load_dotenv()
    access_token = os.getenv('BOT_ACCESS_TOKEN')
    bot_username = os.getenv('BOT_USERNAME')
    bot_name = os.getenv('BOT_NAME')
    bot_id = os.getenv('BOT_ID')
    # print(type(access_token), type(bot_username), type(bot_name), type(bot_id))
    return access_token, bot_username, bot_name, bot_id

def list_webex_rooms(access_token):
    apiUrl = 'https://webexapis.com/v1/rooms'
    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    queryParams = { 'sortBy': 'lastactivity', 'max': '2' }
    response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )
    return response

def post_webex_directMsg(access_token, message, person_email):
    apiUrl = 'https://webexapis.com/v1/messages'
    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    body = { 'toPersonEmail': person_email, 'text': message }
    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )
    return response

def postWebexMsg_md(access_token, person_email, message):
    apiUrl = 'https://webexapis.com/v1/messages'
    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    body = { 'toPersonEmail': person_email, 'markdown': message }
    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )
    return response.status_code

def postWbx_roomMsg_md(access_token, room_id, message):
    apiUrl = 'https://webexapis.com/v1/messages'
    httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
    body = { 'roomId': room_id, 'markdown': message }
    response = requests.post( url = apiUrl, json = body, headers = httpHeaders )
    return response.status_code
### CODE BELOW THIS LINE CAN AND SHOULD BE DELETED

bot_cred = load_dotenv_vars()
# print(bot_cred)
rooms_list = list_webex_rooms(bot_cred[0])
# print(rooms_list.status_code)
print(json.dumps(json.loads(rooms_list.text), indent=4))

webex_messages = [
    '**Warning!!!**',
    '_Warning!!!_',
    '[Danger, Will Robinson!!!](https://en.wikipedia.org/wiki/Lost_in_Space#Catchphrases)'
    ]
room_id = json.loads(rooms_list.text)

for msg in webex_messages:
    webex_user = 'angel.inglese@gmail.com'
    crtl_response = postWbx_roomMsg_md(bot_cred[0], room_id['items'][0]['id'], msg)
