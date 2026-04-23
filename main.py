import os

from dotenv import load_dotenv
from openai import OpenAI

def build_client() -> OpenAI:
    load_dotenv()
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise Exception('OpenAI API key is required.')

    return OpenAI(api_key=api_key)

def get_bot_response(client: OpenAI, message: str) -> str:
    response = client.responses.create(
        model='gpt-4.1-mini',
        input=message,
    )
    return response.output_text


def read_multiline_text() -> str:
    print('Introduce el texto que quieres resumir.')
    print("Cuando termines, escribe 'FIN' en una línea nueva.\n")

    lines = []

    while True:
        line = input()

        if line.strip().upper() == 'FIN':
            break

        lines.append(line)

    return '\n'.join(lines).strip()

def summarize_text(client: OpenAI, text: str) -> str:
    prompt = f'Resume el siguiente texto de forma clara y concisa:\n\n{text}'
    return get_bot_response(client=client, message=prompt)

def main() -> None:
    ai_client = build_client()
    text = read_multiline_text()

    if not text:
        print('No has introducido ningún texto.')
        return

    summary = summarize_text(ai_client, text)
    print(f'\nResumen:\n{summary}')

if __name__ == '__main__':
    main()