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


def get_connection(path_to_secret_json):
    """ get connection to api """
    gc = gspread.service_account(path_to_secret_json)
    return gc
