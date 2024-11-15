import os
from generate_html import setup_openai, generate_html_from_article, save_html_to_file, generate_template_file, generate_preview_file

API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("Klucz API nie został ustawiony. Ustaw zmienną środowiskową OPENAI_API_KEY.")

ARTICLE_FILE_PATH = 'text.txt'
OUTPUT_FILE_PATH = 'artykul.html'

PROMPT_TEXT = """
Przekonwertuj poniższy artykuł na HTML, używając odpowiednich tagów do strukturyzacji tekstu. 
Użyj <h1> dla głównego tytułu, <h2> dla nagłówków oraz <p> dla akapitów. 
Oznacz miejsca na obrazy za pomocą tagu <img src="image_placeholder.jpg" alt="opis obrazu"> oraz dodaj podpis w <figcaption>.
Tylko HTML, bez dodatkowych instrukcji ani elementów spoza treści artykułu. 
Umieść treść artykułu wyłącznie między <body> i </body>.
"""

def main():
    setup_openai(API_KEY)

    with open(ARTICLE_FILE_PATH, 'r', encoding='utf-8') as file:
        article_text = file.read()

    article_html = generate_html_from_article(article_text, PROMPT_TEXT)
    save_html_to_file(article_html, OUTPUT_FILE_PATH)

    generate_template_file()

    generate_preview_file(article_html)

if __name__ == "__main__":
    main()
