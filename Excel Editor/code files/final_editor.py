from editor_logic import edit_sheet
from tqdm import tqdm
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()
#local dir path (source)
dir_path = os.environ['STARTDIR']

#local dir path (end)
end_path = os.environ['ENDDIR']

# get list of all excel files
list_excel = []
for file in os.listdir(dir_path):
    if file.endswith(".xlsx"):
        list_excel.append(file)
list_excel


#call editor function on each sheet, pass in sheet name, original directory, ending directory
#displays progress bar 
for i in tqdm(range(len(list_excel)), desc="Editing Files..."):
    edit_sheet(list_excel[i], dir_path, end_path)