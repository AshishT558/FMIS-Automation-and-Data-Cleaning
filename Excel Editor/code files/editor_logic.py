import pandas as pd
import xlsxwriter
from datetime import datetime

def edit_sheet(file_name, dir_path, end_path):
    sheet = pd.read_excel(dir_path + file_name, header=None)
    sheet.head()

    #remove the first row
    sheet = sheet.iloc[1:]

    #set columns
    sheet.columns = sheet.iloc[0]

    #remove repeat row
    sheet = sheet.iloc[1:]
    sheet.head()

    #get index where column should be added
    column_count = sheet.columns.size

    # get current datetime and
    # format into mm/dd/yyyy hh:mm:ss AM/PM
    now = datetime.now()
    formatted_date = now.strftime("%m/%d/%Y %H:%M:%S %p")

    #add new column with all entries being the datetime
    sheet.insert(column_count, 'Query-Date', formatted_date)

    #get index of last '_' in the file_name - this indicates where the number starts
    index = file_name.rindex('_')
    file_name = file_name[:index] + '.xlsx'

    #export
    writer = pd.ExcelWriter(end_path + file_name, engine='xlsxwriter')
    sheet.to_excel(writer, index=False)
    writer.close()