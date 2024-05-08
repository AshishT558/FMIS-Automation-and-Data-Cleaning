from fmis_manager import downloader
from final_editor_function import editor_func
from tqdm import tqdm
import os
from dotenv import load_dotenv

## SCRIPT TO RETRIEVE QUERIES FROM FMIS ##
## - Retrieves lists of queries specified below ##
## - active lists: pl_daily, matt_data, maha_data ##

## Written by Ashish Thomas 4/10/2024
## Edited by Aishwarya Suryanarayana

#load environment variables
load_dotenv()
user = os.environ['USER']
passw = os.environ['PASSW']

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


#MISC
extra = [
    'MB_GL013_3YEAR_DATA'
]

# Run Maha data queries
# for x in tqdm(range(len(maha_data)), desc="3. Getting Maha files"):
#     downloader(maha_data[x], user, passw)

# # Run P&L Daily Runs
for x in tqdm(range(len(pl_daily)), desc="1. Getting Daily Run Files"):
    downloader(pl_daily[x], user, passw)


# Run Matt data queries
# for x in tqdm(range(len(matt_data)), desc="2. Getting Matt files"):
#     downloader(matt_data[x], user, passw)

# Run EXTRA data queries
# for x in tqdm(range(len(extra)), desc="3. Getting Extra files"):
#     downloader(extra[x], user, passw)
