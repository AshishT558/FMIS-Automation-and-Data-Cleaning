from tqdm import tqdm
import warnings
import os
import glob
from dotenv import load_dotenv
from fmis_manager import downloader
from editor_logic import edit_sheet

# Main Pipeline #
## Written by Ashish Thomas 5/2/2024

#load environment variables
load_dotenv()

#local dir path (source)
dir_path = os.environ['STARTDIR']
#local dir path (end)
end_path = os.environ['ENDDIR']


#P&L Daily Runs
pl_daily = [
    'PL_BUYER_BACKLOG',
    'PL_CHNG_ORDER_INSERTS',
    'PL_CONTRACTS_DAILY',
    'PL_INV_BY_BASE',
    'PL_LEADTIME',
    'PL_OPEN_PO_SUMMARY',
    'PL_PO_ENCUMB_LINE_LEVEL',
    'PL_PO_PARTICIPATION_DBE',
    'PL_PURCH_ORDER_DATA_PT1',
    'PL_PURCH_ORDER_DATA_PT5',
    'PL_PURCH_ORDER_DATA_PT6',
    'PL_PURCH_ORDER_DATA_PT7',
    'PL_PURCH_ORDER_DATA_PT8',
    'PL_RECEIPTS_TO_PO',
    'PL_REQ_ACTIVITY',
    'PL_REQUISITION_DATA',
    'PL_REQUISITION_DATA_PT1',
    'PL_UNPOSTED_VCHR_PYMTS',
    'PL_VOUCHER_PYMTS_CURRFY',
    'PL_WO_DESCRIPTIONS'
]

#Matt data
matt_data = [
    'SLT_AP024_ENGMAINT',
    'SLT_CMS_WO_INTERFACE',
    'SLT_ENG_REQ_TO_PO_MCUN',
    'SLT_GL_COMBO_OPER_BY_DEPTID_DS',
    'SLT_RTBS_PEND_VW',
    'SLT_SRM_DB_RTBS_VW'
]

#Maha data
maha_data = [
    'MB_AP024_1YEAR_DATA',
    'MB_GL013_1YEAR_DATA',
    'MB_GL013_3YEAR_DATA',
]

#list of list of batches
list_batches = [maha_data, pl_daily, matt_data]

#Iterate over all batches, get sheet and edit it for each file in each batch
for batch_num in tqdm(range(len(list_batches)), desc="RUNNING PIPELINE"):
    #For 1 batch
    for file_num in tqdm(range(len(list_batches[batch_num])), desc="Batch " + str(batch_num)):
        file = list_batches[batch_num][file_num]

        #Download from FMIS
        downloader(file)

        #Get File from downloads folder
        for file_to_edit in os.listdir(dir_path):
            if file_to_edit.endswith(".xlsx"):
                file_name = file_to_edit
        
        #Edit sheet
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            edit_sheet(file_name, dir_path, end_path)

        #Remove unedited version from Downloads folder
        os.remove(dir_path + file_name)

    #Print after every batch completes
    print("Finished Batch #{}".format(batch_num))

#Print after all batches completed
print("PIPELINE RUN")