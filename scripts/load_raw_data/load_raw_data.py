import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from tkinter import filedialog, messagebox 
import gui
import sys

#function that opens a file explorer window to choose a file to work on
def file_select():
    while True:
         file_path = filedialog.askopenfilename()
         if os.path.splitext(file_path)[1] != '.csv':
              messagebox.showerror('Wrong file format', 'The file you select must be a csv file.')
              if messagebox.askretrycancel('Retry', 'Would you like to select another file?') == False:
                   sys.exit()
         else:
              messagebox.showinfo('Correct', 'File type correct.')
              break
    return file_path
     
#function that loads data from a csv file to database
def load_data(file_path, connection):
        df = pd.read_csv(file_path)
        try:
            year= gui.final_selection.get('year')
            quarter= gui.final_selection.get('quarter')
        except AttributeError:
            messagebox.showerror('Error', 'No data selected to load. Please select year and quarter.')
            sys.exit()
        df['year'] = year
        df['quarter'] =quarter
        table_name = f'raw_{quarter.lower()}_{year}'
        df.to_sql(table_name, con=connection, if_exists='replace', index=False)
        messagebox.showinfo('Database Connection', 'Database connection successful.')
        messagebox.showinfo('Correct', f'{file_path} loaded to {table_name} table.')
    
def main():
    #loading database info to variables from the .env file
    load_dotenv()
    db_host = os.getenv('POSTGRES_HOST')
    db_port = os.getenv('POSTGRES_PORT')
    db_user = os.getenv('POSTGRES_USER')
    db_password = os.getenv('POSTGRES_PASSWORD')
    db_name = os.getenv('POSTGRES_DB')

    #passing all db info to one string variable
    connection_string = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
    engine = create_engine(connection_string)
    #file selection
    file_path = file_select() 
    gui.create_selection_window()
    #loading data from csv file to the database
    load_data(file_path, engine)
if __name__ == '__main__':
    main()