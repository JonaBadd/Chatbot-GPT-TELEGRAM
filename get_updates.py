import requests
import time

def get_updates(token, offset=None):
    url = f"https://api.telegram.org/bot{INGRESA TU KEY DE TELEGRAMBOT}/getUpdates"
    params = {"offset": offset} if offset else {}
    response = requests.get(url, params=params)
    return response.json()

def print_new_messages(token):
    offset = None
    while True:
        updates = get_updates(token, offset)  # Esta función debe estar definida previamente
        if "result" in updates:
            for update in updates["result"]:
                message = update["message"]
                id = message["from"]["id"]
                username = message["from"]["first_name"]
                text = message.get("text")
                print(f"Usuario: {username} ({id})")
                print(f"Mensaje: {text}")
                print("---")
                offset = update["update_id"] + 1  # Corrección aquí
        time.sleep(1)

token = "TELEGRAM_TOKEN"
print_new_messages(token)
