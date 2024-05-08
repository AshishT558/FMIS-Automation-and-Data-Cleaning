from tqdm import tqdm
import warnings
import os
import glob
from dotenv import load_dotenv
from fmis_manager import downloader
from editor_logic import edit_sheet

#load environment variables
load_dotenv()

#username for FMIS
user = os.environ['USER']
#password for FMIS
passw = os.environ['PASSW']

#local dir path (source)
dir_path = os.environ['STARTDIR']
#local dir path (end)
end_path = os.environ['ENDDIR']

list_excel = []
for file in os.listdir(dir_path):
    if file.endswith(".xlsx"):
        list_excel.append(file)
        os.remove(dir_path + file)