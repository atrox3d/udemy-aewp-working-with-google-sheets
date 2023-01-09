import gspread
from gspread.exceptions import *
import statistics

import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet(gc, 'weather_private')
worksheet_1: gspread.worksheet.Worksheet = spreadsheet.worksheet('2013')
ws1 = worksheet_1

# print(ws1.col_count)
# print(ws1.row_count)
g = [float(x) for x in ws1.col_values(7)[1:]]
print(g)
mean = round(statistics.mean(g), 2)
print(mean)
ws1.update('G26', mean)
