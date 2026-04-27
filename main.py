import os

from dotenv import load_dotenv
from openai import OpenAI


def build_client() -> OpenAI:
    load_dotenv()
    api_key_openai = os.getenv("OPENAI_API_KEY")

    if not api_key_openai:
        raise ValueError("OpenAI API key is required")

    return OpenAI(api_key=api_key_openai)


def get_bot_response(client: OpenAI, text: str) -> str:
    response = client.responses.create(
        model='gpt-4.1-mini',
        input=text,
    )
    return response.output_text


def ideas_bot_response(client: OpenAI, text: str) -> str:
    prompt = f"""Dame 5 ideas sobre el siguiente tema:

    {text}

    Para cada idea usa EXACTAMENTE este formato:

    1. Nombre:
    2. Descripción:
    3. Nivel de dificultad (bajo, medio, alto).
     
    No añadas texto fuera de este formato.
    Responde en español.
    """
    return get_bot_response(client, prompt)


def get_text() -> str:
    text = input("Introduce un tema: ")
    return text.strip()


def main() -> None:
    print('=== AI Idea Generator ===')
    client = build_client()
    text = get_text()

    if not text:
        return
    response = ideas_bot_response(client, text)
    print(f'Ideas generadas:')
    print(response)

if __name__ == '__main__':
    main()