"""
- https://console.cloud.google.com/
- "CREATE PROJECT" (automate with python)

-------------------------------------------------------------------
GOOGLE DRIVE API
-------------------------------------------------------------------

- "+ ENABLE APIS AND SERVICES"
- search for "google drive api"
- select "Google Drive API"
- ENABLE
- CREATE CREDENTIALS
- Select an API: "Google Drive API"
- Select "Application data"
- Select "No, i'm not using them"
- NEXT
- Service account name: (Automate with Python Account)
- CREATE AND CONTINUE
- Role: Project/Editor
- CONTINUE
- Automate with Python Account: skip/ DONE
- Credentials/Service Accounts: click on account
- KEYS
- ADD KEY/Create new key
- JSON, CREATE
- save json

-------------------------------------------------------------------
GOOGLE SHEETS API
-------------------------------------------------------------------

- burger menu
- APIs & Services
- "+ ENABLE APIS AND SERVICES"
- search for "google sheets api"
- select "Google Sheets API"
- ENABLE

-------------------------------------------------------------------
GOOGLE SHEETS
-------------------------------------------------------------------
- open private sheet
- share
- use mail address from JSON file
- select Editor
- Send
"""

import gspread
import re

###########################################################
# get connection to api
###########################################################
gc = gspread.service_account('secret/google-drive-api.json')

###########################################################
# get spreadsheet
###########################################################
spreadsheet = gc.open('weather_private')

###########################################################
# get worksheet by index
###########################################################
worksheet_1 = spreadsheet.get_worksheet(0)
print(worksheet_1)

###########################################################
# get worksheet by name
###########################################################
worksheet_1 = spreadsheet.worksheet('2013')
print(worksheet_1)

###########################################################
# get data
###########################################################
data = worksheet_1.get_all_records()
print(data[0])
# for row in data:
#     print(row)

###########################################################
# get a row (with list unpacking)
###########################################################
[a5e5] = worksheet_1.get_values('a5:e5')
print(f'{a5e5=}')

###########################################################
# get rows
###########################################################
a5f7 = worksheet_1.get_values('a5:f7')
print(f'{a5f7=}')

###########################################################
# get rows with list unpacking
###########################################################
[a5f5, a6f6, a7f7] = worksheet_1.get_values('a5:f7')
print(f'{a5f5=}')
print(f'{a6f6=}')
print(f'{a7f7=}')

###########################################################
# get column by coordinates
###########################################################
ws1 = worksheet_1
column = ws1.get_values('c:c')
print(f'{column=}')

###########################################################
# get column values
###########################################################
col = ws1.col_values(2)
print(f'{col=}')

###########################################################
# get row values
###########################################################
row = ws1.row_values(6)
print(f'{row=}')

###########################################################
# get cell value
###########################################################
cell = ws1.get_values('D5')
print(f'{cell=}')

###########################################################
# get cell value with slicing
###########################################################
cell = ws1.get_values('D5')[0][0]
print(f'{cell=}')

###########################################################
# get cell value with list unpacking
###########################################################
[[cell]] = ws1.get_values('D5')
print(f'{cell=}')

###########################################################
# get direct cell value
###########################################################
cell = ws1.acell('D5')
print(f'{cell=}')

###########################################################
# get direct cell value
###########################################################
cell = ws1.acell('D5').value
print(f'{cell=}')

###########################################################
# get cell properties
###########################################################
row = ws1.acell('D5').row
col = ws1.acell('D5').col
address = ws1.acell('D5').address
print(f'{row=}, {col=}, {address=}')

###########################################################
# search for a cell
###########################################################
find = ws1.find('-10')
print(f'{find=}')

###########################################################
# search for all cells
###########################################################
findall = ws1.findall('-9')
print(f'{findall=}')
for cell in findall:
    print(f'{cell.row=}, {cell.col=} = {cell.value=}')

###########################################################
# search for partial match using regex
###########################################################
regex = re.compile('99')
findall = ws1.findall(regex)
print(f'regex: {findall=}')
for cell in findall:
    print(f'regex: {cell.address=} | {cell.row=}, {cell.col=} = {cell.value=}')
