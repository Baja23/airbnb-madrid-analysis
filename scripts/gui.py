import tkinter as tk
from tkinter import ttk
import sys

# --- Zmienne Globalne ---
# Dodajemy pole 'action', aby wiedzieć, co użytkownik chce zrobić dalej
final_selection = {
    'year': None,
    'quarter': None,
    'action': None  # Nowe pole: 'finish' lub 'next'
}

def create_selection_window():
    """
    Tworzy i uruchamia okno dialogowe do wyboru roku i kwartału.
    """
    
    root = tk.Tk()
    root.title("Wybór Danych do Załadowania")
    root.geometry("350x300")
    root.resizable(False, False)
    root.attributes('-topmost', True)
    
    selected_year = tk.StringVar()
    selected_quarter = tk.StringVar()
    
    YEAR_OPTIONS = ['2020', '2021', '2022', '2023', '2024', '2025', '2026', '2027']
    QUARTER_OPTIONS = ['Q1', 'Q2', 'Q3', 'Q4']
    
    # --- Dropdown dla Roku ---
    year_frame = ttk.Frame(root)
    year_frame.pack(pady=20) 
    
    year_label = ttk.Label(year_frame, text="Select Year:")
    year_label.pack(side=tk.LEFT, padx=5)
    
    year_combobox = ttk.Combobox(
        year_frame,
        textvariable=selected_year,
        values=YEAR_OPTIONS,
        state='readonly'
    )
    year_combobox.pack(side=tk.LEFT)
    year_combobox.current(0)
    
    # --- Radio Buttons dla Kwartału ---
    quarter_frame = ttk.LabelFrame(root, text="Select quarter:")
    quarter_frame.pack(padx=20, pady=10, fill='x')
    
    for quarter in QUARTER_OPTIONS:
        rb = ttk.Radiobutton(
            quarter_frame,
            text=quarter,
            variable=selected_quarter,
            value=quarter
        )
        rb.pack(anchor='w', padx=10)
        
    selected_quarter.set('Q1')
    
    # --- KROK 5: Logika Przycisków ---
    
    def save_and_close(action_type):
        """Wspólna funkcja do zapisywania danych i zamykania okna."""
        final_selection['year'] = selected_year.get()
        final_selection['quarter'] = selected_quarter.get()
        final_selection['action'] = action_type # Zapisujemy, który guzik kliknięto
        root.destroy()

    # Funkcje pomocnicze dla przycisków
    def on_confirm():
        save_and_close('finish')

    def on_load_next():
        save_and_close('next')
    
    # --- KROK 6: Układ Przycisków ---
    
    # Ramka na przyciski, żeby były w jednej linii
    button_frame = ttk.Frame(root)
    button_frame.pack(pady=30)

    # Przycisk "Załaduj kolejny"
    next_button = ttk.Button(button_frame, text="Load Next File", command=on_load_next)
    next_button.pack(side=tk.LEFT, padx=10)

    # Przycisk "Zatwierdź"
    submit_button = ttk.Button(button_frame, text="Confirm & Finish", command=on_confirm)
    submit_button.pack(side=tk.LEFT, padx=10)

    root.mainloop()

# --- Testowanie (tylko do podglądu, usuń w głównej aplikacji) ---
if __name__ == "__main__":
    create_selection_window()
    print(f"Wybrano: {final_selection}")