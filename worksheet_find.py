import re

import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet(gc, 'weather_private')
worksheet_1 = spreadsheet.worksheet('2013')
ws1 = worksheet_1

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
