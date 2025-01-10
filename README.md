## Konwersja Artykułu na HTML z Wykorzystaniem OpenAI API

Aplikacja Python służąca do automatycznej konwersji artykułu tekstowego do formatu HTML z użyciem OpenAI API. Projekt składa się z trzech głównych modułów: `main.py`, `generate_html.py` oraz pliku tekstowego `text.txt` zawierającego artykuł. Wynikiem działania jest wygenerowany dokument HTML (`artykul.html`) oraz pełny podgląd (`podglad.html`), korzystający z szablonu (`szablon.html`) wzbogaconego o formatowanie CSS.

### Pliki projektu
- **main.py**: Główny skrypt zarządzający konwersją i generowaniem plików wynikowych.

#### Pliki wejściowe (do przygotowania przez użytkownika):
- **text.txt**: Plik tekstowy zawierający treść artykułu do konwersji. Umieść ten plik w katalogu głównym projektu.

#### Pliki generowane automatycznie (podczas działania programu):
- **generate_html.py**: Moduł zawierający funkcje do konwersji tekstu na HTML z użyciem OpenAI API, generowania szablonu oraz podglądu artykułu.
- **artykul.html**: Wynikowy plik HTML zawierający skonwertowany artykuł bez stylizacji.
- **szablon.html**: Szablon HTML z wbudowanym CSS, służący do wizualizacji artykułu.
- **podglad.html**: Pełny podgląd artykułu z formatowaniem i strukturą HTML.

### Wymagania

- Python 3.6 lub wyższy
- Konto OpenAI i klucz API, który musi być ustawiony jako zmienna środowiskowa `OPENAI_API_KEY`

### Instalacja

1. Sklonuj repozytorium lub pobierz kod źródłowy projektu.
   
```bash
   git clone <URL_REPO>
   cd <NAZWA_FOLDERU>
```

2. Zainstaluj wymagane biblioteki:

```bash
  pip3 install openai
```
 
3. Ustaw zmienną środowiskową OPENAI_API_KEY, wstawiając swój klucz API.
Na systemie Windows:
```bash
  set OPENAI_API_KEY=twój_klucz_api
```

Na systemie Linux/Mac:
```bash
  export OPENAI_API_KEY=twój_klucz_api
```

### Instrukcja uruchomienia

1. Umieść treść artykułu do konwersji w pliku text.txt.
2. Uruchom main.py, aby wygenerować pliki HTML:
```bash
  python3 main.py
```
3. Po uruchomieniu skryptu zostaną wygenerowane następujące pliki:
artykul.html: Skonwertowany artykuł w HTML.
szablon.html: Szablon HTML zawierający CSS, umożliwiający estetyczne wyświetlanie artykułu.
podglad.html: Końcowy podgląd artykułu z szablonem CSS, który można otworzyć w przeglądarce.

### Struktura działania

1. Konfiguracja API: Skrypt main.py wczytuje klucz API OpenAI oraz treść artykułu z text.txt.
2. Konwersja artykułu do HTML: generate_html_from_article w generate_html.py wysyła treść artykułu do modelu OpenAI, który zwraca sformatowany HTML.
3. Generowanie szablonu: generate_template_file tworzy plik szablon.html zawierający CSS, ale bez treści artykułu.
4. Tworzenie podglądu: generate_preview_file łączy zawartość szablon.html i artykul.html w jeden plik podglad.html, umożliwiając wizualne zapoznanie się z efektem końcowym.

### Przykładowe zastosowania

- Automatyczna konwersja artykułów lub dokumentów na HTML.
- Generowanie treści blogów lub artykułów do wstawienia na strony internetowe.
- Szybkie tworzenie stron lub dokumentacji z wyjściem w formacie HTML.

### Uwagi

Pamiętaj, aby nie udostępniać swojego klucza API publicznie.
Jeśli treść w podglad.html zawiera powtarzające się sekcje lub niepożądane elementy, możesz dostosować prompt w main.py.
