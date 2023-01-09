import gspread

import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet(gc, 'weather_private')
worksheet_1: gspread.worksheet.Worksheet = spreadsheet.worksheet('2013')
print(type(worksheet_1))
ws1 = worksheet_1


# update a cell A1 coordinate system
ws1.update('E5', -29)

# update a cell RC coordinate system
ws1.update_cell(row=5, col=5, value=-39)
