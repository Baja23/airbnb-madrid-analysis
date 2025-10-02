Analiza cen Airbnb w Madrycie

Analiza danych z Inside Airbnb za okres 12 ostatnich miesięcy (pierwszy plik jest z 12.09.2024, ostatni z 12.06.2025). Celem projektu jest przeanalizowanie tego jak różne czynniki (dzielnica, status Superhosta, typ pokoju/nieruchomości, etc.) wpływają na ceny ofert. Raport ten ma za zadanie pomóc potencjalnym inwestorom w wyborze odpowiedniej nieruchomości oraz ustaleniu ceny wynajmu zgodnej z rynkiem.

Jak Uruchomić (Setup & Usage) - instrukcja krok po kroku: 
    Sklonuj repozytorium. 
    Stwórz i aktywuj środowisko wirtualne (python -m venv venv, source ...).
    Zainstaluj zależności (pip install -r requirements.txt).
    Uruchom bazę danych (docker-compose up -d).
    Uruchom potok danych (python scripts/load_raw_data.py, etc.).
