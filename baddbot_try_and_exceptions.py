import requests
import time
from openai import OpenAI

openai = OpenAI(api_key='INSERTA TU API KEY')
TOKEN = "INSERTA TU KEY TELEGRAMBOT"

def get_updates(offset):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"timeout": 100, "offset": offset}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Lanza una excepción si hay un error en la solicitud
        data = response.json()
        if "result" in data:
            return data["result"]
        else:
            print("No updates found.")
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching updates: {e}")
        return []

def send_messages(chat_id, text):
    url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    params = {"chat_id": chat_id, "text": text}
    response = requests.post(url, params=params)
    return response

def get_openai_response(prompt):
    system = '''
        Eres un asistente de atención a clientes 
        y estudiantes de la plataforma de educación online en tecnología,  
        inglés y liderazgo llamada Platzi
        '''     
    response = openai.chat.completions.create(
		model='INGRESA EL NOMBRE DE TU MODELO CON FINE-TUNING',
		messages=[
            {"role": "system", "content" :f'{system}'},
            {"role": "user", "content" : f'{prompt}'}],
		max_tokens=150,
		n=1,
        stop="END", # Esta línea evita que se repita el texto
		temperature=0.2)
    return response.choices[0].message.content.strip()

def main():
    print("Starting bot...")
    offset = 0
    try:
        while True:
            updates = get_updates(offset)
            if updates:
                for update in updates:
                    offset = update["update_id"] + 1
                    chat_id = update["message"]["chat"]["id"]
                    user_message = update["message"]["text"]
                    print(f"Received message: {user_message}")
                    GPT = get_openai_response(user_message)
                    send_messages(chat_id, GPT)
            else:
                time.sleep(1)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
