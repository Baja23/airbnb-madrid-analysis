# Analiza ofert wynajmu krótkoterminowego z serwisu Airbnb na przykładzie Madrytu

## 1. Opis projektu
### Cel projektu: 
Zbadanie wpływu różnych cech (np. pora roku, dzielnica czy oceny) na cenę za wynajem w Madrycie. Stworzenie dashboardu informacyjnego dla potencjalnych inwestorów, którzy chcieliby rozpocząć przygodę z najmem krótkoterminowym w Madrycie. 
### Wybrane technologie: 
Baza danych PostgreSQL postawiona na Dockerze, ETL oraz analiza danych za pomocą Pythona, dashboard w PowerBI. 

Dane pochodzą z serwisu Inside Airbnb i dotyczą okresu od września 2024 do września 2025. 
Skrypty w Pythonie mogą zostać wykorzystane do ETL oraz analizy danych dotyczących innych miast o ile będą pobrane z serwisu Inside Airbnb. Dashboard po lekkich modyfikacjach również może zostać wykorzystany do danych dotyczących innych miast. 

## 2. Jak Uruchomić?
    Sklonuj repozytorium. 
    Stwórz i aktywuj środowisko wirtualne (python -m venv venv).
    Zainstaluj zależności (pip install -r requirements.txt).
    Uruchom bazę danych (docker-compose up -d).
    Uruchom potok danych (python scripts/load_data.py).
    Dodaj ręcznie pliki csv, z których chcesz załadować dane.
    Po załadowaniu plików do bazy danych uruchom notatnik notebooks/basic_eda.ipynb
    Po wykonaniu się notatnika, oczyszczone dane zostaną zapisane do data/clean_data.parquet
    Na podstawie takiego pliku parquet został stworzony dashboard w PowerBI dla danych z Madrytu
