import tkinter as tk
from tkinter import ttk # Importujemy 'themed' widżety
import sys

# --- Zmienne Globalne do Przechowywania Wyboru ---
# Używamy ich, aby móc uzyskać do nich dostęp po zamknięciu okna
final_selection = {
    'year': None,
    'quarter': None
}

def create_selection_window():
    """
    Tworzy i uruchamia okno dialogowe do wyboru roku i kwartału.
    """
    
    root = tk.Tk()
    root.title("Wybór Danych do Załadowania")
    root.geometry("350x300") # Ustawiamy rozmiar okna
    root.resizable(False, False) # Blokujemy możliwość zmiany rozmiaru
    root.attributes('-topmost', True)  # Ustawiamy okno na wierzchu
    
    # --- KROK 2: Zmienne Kontrolne ---
    selected_year = tk.StringVar()
    selected_quarter = tk.StringVar()
    
    # Definicja opcji
    YEAR_OPTIONS = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027'] # Możesz je dynamicznie generować
    QUARTER_OPTIONS = ['Q1', 'Q2', 'Q3', 'Q4']
    
    # --- KROK 3: Dropdown dla Roku ---
    
    # Ramka do grupowania etykiety i listy
    year_frame = ttk.Frame(root)
    year_frame.pack(pady=20) 
    
    year_label = ttk.Label(year_frame, text="Select")
    year_label.pack(side=tk.LEFT, padx=5)
    
    year_combobox = ttk.Combobox(
        year_frame,
        textvariable=selected_year,
        values=YEAR_OPTIONS,
        state='readonly' # Użytkownik nie może wpisać własnej wartości
    )
    year_combobox.pack(side=tk.LEFT)
    year_combobox.current(0) # Ustawia domyślnie pierwszą opcję
    
    # --- KROK 4: Radio Buttons dla Kwartału ---
    
    # Ramka z etykietą
    quarter_frame = ttk.LabelFrame(root, text="Select quarter:")
    quarter_frame.pack(padx=20, pady=10, fill='x')
    
    # Tworzymy przyciski w pętli
    for quarter in QUARTER_OPTIONS:
        rb = ttk.Radiobutton(
            quarter_frame,
            text=quarter,
            variable=selected_quarter, # Wszystkie łączą się z tą samą zmienną
            value=quarter  # Każdy ma unikalną wartość
        )
        rb.pack(anchor='w', padx=10) # anchor='w' (west) wyrównuje do lewej
        
    selected_quarter.set('Q1') # Ustawiamy domyślny wybór
    
    # --- KROK 5: Przycisk Zatwierdzenia ---
    
    def on_submit():
        """Pobiera wartości i zamyka okno."""
        # Zapisujemy wybór do globalnego słownika
        final_selection['year'] = selected_year.get()
        final_selection['quarter'] = selected_quarter.get()
        # Zamykamy okno
        root.destroy()
    
    submit_button = ttk.Button(root, text="Confirm and load", command=on_submit)
    submit_button.pack(pady=30)
    root.mainloop()