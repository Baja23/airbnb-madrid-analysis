import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import tkinter
from tkinter import filedialog, messagebox 

#function that opens a file explorer window to choose a file to work on
def file_select():
    while True:
         file_path = filedialog.askopenfilename()
         if os.path.splitext(file_path)[1] != '.csv':
              messagebox.showerror('Wrong file format', 'The file you select must be a csv file.')
              if messagebox.askretrycancel('Retry', 'Would you like to select another file?') == False:
                   exit()
         else:
              print('File type correct.')
              break
    return file_path

#function that does assertion testing before loading the data
def data_quality_check(file_path):
     df_file = pd.read_csv(file_path)

     #Uniqueness test
     if not df_file['id'].is_unique:
          duplicate_rows = df_file[df_file['id'].duplicated(keep=False)] #saving all duplicate id rows
          error_message =f'Error! id column contains duplicates. \nNumber of duplicate columns: {len(duplicate_rows)} \n'
          messagebox.showerror(f'Error! id column contains duplicates.')
          raise AssertionError('Quality check failed \n', error_message)

     #Completeness test
     required_columns = ['host_id', 'price', 'neighbourhood_cleansed'] #list of key columns 
     df_mask = df_file[required_columns].isnull()
     if df_mask.values.any():
          missing_values = df_mask.sum()
          error_details = missing_values[missing_values > 0].to_string()
          error_message2 = f'Error! Missing values foud in the key columns. \n {error_details}'
          messagebox.showerror('Error! Missing values found in the key coulmns.')
          raise AssertionError('Quality check failed \n', error_message2)
     
     #Range/Validity test
     #Price
     invalid_rows = df_file.query('price <= 0')
     if not invalid_rows.empty:
          error_message3 = (f'Error! Invalid price range. \n{len(invalid_rows)} rows with price being <= 0 \n'
                            f'First 5 invalid price rows: \n'
                            f'{invalid_rows[['id', 'price']].head(5).to_string()}')
          messagebox.showerror('Quality check failed', error_message3)
          raise AssertionError(error_message3)
     
     #Longitude/Latitude
     invalid_longitude = ~df_file['longitude'].between(-180, 180)
     invalid_latitude = ~df_file['latitude'].between(-90, 90)
     invalid_geo_mask = invalid_longitude | invalid_latitude 
     if invalid_geo_mask.any():
          error_message4 = (f'Error! Invalid geographical information. \n'
          f'{len(invalid_geo_mask)} rows incorrect. \n'
          f'{df_file[invalid_geo_mask['id', 'longitude', 'latitude']]}')
          messagebox.showerror(error_message4)

def Load_to_quarantine_table(df_file, engine, reason):
     messagebox.showinfo('Quarantine', f'Moving file to a quarantine table. Reason: {reason}')
     df_file['quarantine_reason'] = reason
     df_file.to_sql('raw_data_quaratined', con=engine, if_exists='append', index=False)

     
#function that loads data from a csv file to database
def load_data(file_path, connection):
        df = pd.read_csv(file_path)
        messagebox.showinfo('Correct', 'File read correctly.')
        while True: 
            year= input('Please enter the year associated with this data in the format YYYY: ')
            if len(year) == 4 and year.isdigit() and year[0] + year[1] == '20':
                df['year'] = year
                break
            else:
                print('Year must be in the format YYYY (e.g., 2023).')
        while True:
            quarter= input('Please enter the quarter associated with this data in the format QX (X being the quarter number): ').capitalize()
            if quarter in ['Q1', 'Q2', 'Q3', 'Q4']:
                df['quarter'] = quarter
                break
            else:
                print('Quarter must be in the format QX where X is the quarter number (1-4).')
        table_name = 'raw' + '_' + df.iloc[0]['quarter'] + '_' + df.iloc[0]['year']
        df.to_sql(table_name, con=connection, if_exists='replace', index=False)
        messagebox.showinfo('Correct', f'File loaded to {table_name} table.')
    
def main():
    #creating a tkinter object and hidding the main window
    root = tkinter.Tk()
    root.withdraw()
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
    try:
          #loading data from csv file to the database
          load_data(file_path, engine)
    except AssertionError as e: 
         messagebox.showerror('Warning!', 'Quality tests have failed')
         Load_to_quarantine_table()
         root.destroy()
if __name__ == '__main__':
    main()