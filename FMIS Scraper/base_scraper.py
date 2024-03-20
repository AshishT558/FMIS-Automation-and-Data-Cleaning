from fmis_manager import downloader
from tqdm import tqdm
import os
from dotenv import load_dotenv

#load environment variables
load_dotenv()
user = os.environ['USER']
passw = os.environ['PASSW']

#list of all queries to download
list_queries = [
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

#extras
extras = [
    'SLT_AP024_ENGMAINT',
    'SLT_CMS_WO_INTERFACE',
    'SLT_ENG_REQ_TO_PO_MCUN',
    'SLT_GL_COMBO_OPER_BY_DEPTID_DS',
    'SLT_RTBS_PEND_VW',
    'SLT_SRM_DB_RTBS_VW'
]

#non daily run queries
new_queries = [
    'PL_WF_PO_APPR_HISTORY',
    'PL_WF_PO_APPR_FULL_STEPS_V2',
    'PL_VOUCHER_PYMTS_PT7',
    'PL_PURCH_ORDER_DATA_PT4',
    'PL_PURCH_ORDER_DATA_PT3',
    'PL_PURCH_ORDER_DATA_PT0b',
    'PL_PURCH_ORDER_DATA_PT2',
    'PL_PURCH_ORDER_DATA_PT0a',
    'PL_CNT_ACTIVITY',
    'MB_IN_QMAX'
]



for x in tqdm(range(len(extras))):
    downloader(extras[x], user, passw)



# for x in tqdm(range(len(new_queries))):
#     downloader(new_queries[x], user, passw)