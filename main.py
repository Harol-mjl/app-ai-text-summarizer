import os
import json

from dotenv import load_dotenv
from openai import OpenAI


def build_client() -> OpenAI:
    load_dotenv()
    api_key_openai = os.getenv("OPENAI_API_KEY")

    if not api_key_openai:
        raise ValueError("OpenAI API key is required")

    return OpenAI(api_key=api_key_openai)


def get_bot_response(client: OpenAI, prompt: str) -> str:
    response = client.responses.create(
        model='gpt-4.1-mini',
        input=prompt,
    )
    return response.output_text


def translate_text(
        client: OpenAI,
        text: str,
        dst_lang: str,
        tone: str,
) -> str:
    prompt = f"""Traduce este texto {text} en este idioma {dst_lang} y con este tono {tone}
    Solo quiero la traduccion no incluyas nada mas
    """
    return get_bot_response(client=client, prompt=prompt.strip())


def get_text() -> str:
    text = input("Introduce un texto a traducir: ")
    return text.strip()


def get_dst_lang() -> str:
    text = input("Introduce idioma destino: ")
    return text.strip().lower()


def get_tone() -> str:
    text = input("Introduce tono: ")
    return text.strip().lower()


def main() -> None:
    print('=== AI smart Translator ===')
    client = build_client()
    text = get_text()
    dst_lang = get_dst_lang()
    tone = get_tone()

    if not text:
        print("No has introducido texto")
        return

    if not dst_lang:
        print("No has introducido lenguaje destino")
        return

    if not tone:
        tone = "natural"
    
    response = translate_text(client, text, dst_lang, tone)
    print(f"Traduccion: {response}")
if __name__ == '__main__':
    main()