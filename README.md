# FMIS Pipeline

The basics of a data pipline under construction for the MBTA Procurement and Logistics Department. - Pulls data via Selenium from their online site, FMIS, in the form of excel files. These are edited and cleaned to make them inputs for Tableau Prep flows that run daily. 

Steps: 

1. Initiate batches of files to be retrieved from FMIS
2. Run batch retrieval for one batch, sending un-edited files to source directory
3. Edit all files in the batch, sending edited files to target directory
4. Clear all files from source directory
5. Run steps 2-4 for all batches initiated in step 1
