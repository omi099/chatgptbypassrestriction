import os
import json
import requests

API_KEY_FILE = 'api_key.txt'

if os.path.exists(API_KEY_FILE):
    with open(API_KEY_FILE) as f:
        api_key = f.read().strip()
else:
    api_key = input("API: ")
    with open(API_KEY_FILE, 'w') as f:
        f.write(api_key)

while True:
    write = input("Ask me anything: ")

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        'model': 'text-davinci-003',
        'prompt': write,
        'max_tokens': 4000,
        'temperature': 1.0
    }

    response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=data)

    if response.status_code == 200:
        response_data = json.loads(response.text)
        text = response_data['choices'][0]['text']
        print(text)
    else:
        print('API error')
    
    choice = input("Want to ask something else? [y/n]: ")
    if choice.lower() != 'y':
        break
