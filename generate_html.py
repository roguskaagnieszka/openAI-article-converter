import openai
import re


def setup_openai(api_key):
    """Konfiguracja klucza API OpenAI"""
    openai.api_key = api_key


def generate_html_from_article(article_text, prompt_text):
    """Generuje HTML z artykułu na podstawie zadanego promptu"""
    messages = [
        {"role": "system", "content": "Jesteś pomocnym asystentem, który konwertuje artykuły na HTML."},
        {"role": "user", "content": f"{prompt_text}\n\nArtykuł:\n{article_text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=2048,
        temperature=0.7
    )
    html_content = response.choices[0].message['content'].strip()

    # Ekstrakcja zawartości między znacznikami <body> i </body>
    body_content = re.search(r'<body>(.*?)</body>', html_content, re.DOTALL)
    return body_content.group(1) if body_content else html_content


def save_html_to_file(html_content, file_path):
    """Zapisuje zawartość HTML do pliku"""
    with open(file_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    print(f"Plik HTML został zapisany w: {file_path}")


def generate_template_file():
    """Generuje szablon HTML zawierający CSS bez treści artykułu"""
    template_content = """<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Szablon Artykułu</title>
    <link href="https://fonts.googleapis.com/css2?family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Open Sans', sans-serif; line-height: 1.6; padding: 20px; }
        h1, h2, h3 { color: #333; }
        p { margin-bottom: 1em; }
        img { max-width: 100%; height: auto; display: block; margin: 20px 0; }
        figcaption { font-size: 0.9em; color: #555; text-align: center; }
    </style>
</head>
<body>
    <!-- Treść artykułu -->
</body>
</html>"""
    save_html_to_file(template_content, "szablon.html")
    print("Szablon HTML został zapisany w pliku szablon.html.")


def generate_preview_file(article_html):
    """Generuje pełny podgląd HTML, łącząc artykuł z szablonem"""
    with open("szablon.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    # Wstawienie artykułu do szablonu
    preview_content = template_content.replace("<!-- Treść artykułu -->", article_html)

    save_html_to_file(preview_content, "podglad.html")
    print("Podgląd artykułu został zapisany w pliku podglad.html.")
