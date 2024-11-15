import os
from generate_html import setup_openai, generate_html_from_article, save_html_to_file, generate_template_file, generate_preview_file

# Pobierz klucz API z ustawień środowiskowych
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    raise ValueError("Klucz API nie został ustawiony. Ustaw zmienną środowiskową OPENAI_API_KEY.")

# Ścieżki do plików
ARTICLE_FILE_PATH = 'text.txt'
OUTPUT_FILE_PATH = 'artykul.html'

# Prompt do generowania HTML z artykułu
PROMPT_TEXT = """
Przekonwertuj poniższy artykuł na HTML, używając odpowiednich tagów do strukturyzacji tekstu. 
Użyj <h1> dla głównego tytułu, <h2> dla nagłówków oraz <p> dla akapitów. 
Oznacz miejsca na obrazy za pomocą tagu <img src="image_placeholder.jpg" alt="opis obrazu"> oraz dodaj podpis w <figcaption>.
Tylko HTML, bez dodatkowych instrukcji ani elementów spoza treści artykułu. 
Umieść treść artykułu wyłącznie między <body> i </body>.
"""

def main():
    # Inicjalizacja OpenAI API
    setup_openai(API_KEY)

    # Wczytaj treść artykułu z pliku text.txt
    with open(ARTICLE_FILE_PATH, 'r', encoding='utf-8') as file:
        article_text = file.read()

    # Generowanie treści HTML z artykułu
    article_html = generate_html_from_article(article_text, PROMPT_TEXT)
    save_html_to_file(article_html, OUTPUT_FILE_PATH)

    # Generowanie szablonu
    generate_template_file()

    # Tworzenie podglądu artykułu z szablonem
    generate_preview_file(article_html)

if __name__ == "__main__":
    main()
