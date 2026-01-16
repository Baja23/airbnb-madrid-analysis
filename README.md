Jak Uruchomić (Setup & Usage) - instrukcja krok po kroku: 
    Sklonuj repozytorium. 
    Stwórz i aktywuj środowisko wirtualne (python -m venv venv).
    Zainstaluj zależności (pip install -r requirements.txt).
    Uruchom bazę danych (docker-compose up -d).
    Uruchom potok danych (python scripts/load_data.py).
    Dodaj ręcznie pliki csv, z których chcesz załadować dane.
    Po załadowaniu plików do bazy danych uruchom notatnik notebooks/basic_eda.ipynb
    Po wykonaniu się notatnika, oczyszczone dane zostaną zapisane do data/clean_data.parquet
    Na podstawie takiego pliku parquet został stworzony dashboard w PowerBI dla danych z Madrytu