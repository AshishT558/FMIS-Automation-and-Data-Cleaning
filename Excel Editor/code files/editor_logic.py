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

    #rename file to remove extra numbers in name
    #get index of last '_' in the file_name - this indicates where the number starts
    index = file_name.rindex('_')
    file_name = file_name[:index] + '.xlsx'

     #add new column with all entries being the datetime
    # for open_po_summary use PO - Query Date
    # for buyer_backlog use BL - Query Date
    custom_query_date = ''
    if file_name == 'PL_OPEN_PO_SUMMARY.xlsx':
        custom_query_date = 'PO - Query Date'
    elif file_name == 'PL_BUYER_BACKLOG.xlsx':
        custom_query_date = 'BL - Query Date'
    else:
        custom_query_date = 'Query Date'
    sheet.insert(column_count, custom_query_date, formatted_date)

    #export
    writer = pd.ExcelWriter(end_path + file_name, engine='xlsxwriter')
    sheet.to_excel(writer, sheet_name="sheet1", index=False)

    #get the xlsx writer workbook and worksheet objects
    workbook = writer.book
    worksheet = writer.sheets["sheet1"]

    #adjust the column widths based on the content
    for i, col in enumerate(sheet.columns):
        width = max(sheet[col].apply(lambda x: len(str(x))).max(), len(col))
        worksheet.set_column(i, i, width)
        
    writer.close()