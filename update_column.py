import gspread
from gspread.exceptions import *

import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet(gc, 'weather_private')
worksheet_1: gspread.worksheet.Worksheet = spreadsheet.worksheet('2013')
ws1 = worksheet_1

existing_column = ws1.get_values('E2:E25')
print(f'{existing_column=}')

farheneit = [round(float(i) * 9 / 5 + 32, 2) for [i] in existing_column]
farheneit = [[i] for i in farheneit]
print(f'{farheneit=}')

while True:     # retry
    try:
        ws1.update('G1:G25', [['farheneit']] + farheneit)
        break
    except APIError as e:
        print(type(e), e)
        ws1.add_cols(1)
