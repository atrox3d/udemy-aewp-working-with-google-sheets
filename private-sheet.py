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

# get connection to api
gc = gspread.service_account('secret/google-drive-api.json')

# get spreadsheet
spreadsheet = gc.open('weather_private')

# get worksheet by index
worksheet_1 = spreadsheet.get_worksheet(0)
print(worksheet_1)

# get worksheet by name
worksheet_1 = spreadsheet.worksheet('2013')
print(worksheet_1)

# get data
data = worksheet_1.get_all_records()
print(data[0])
for row in data:
    print(row)

