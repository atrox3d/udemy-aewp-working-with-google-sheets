import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet(gc, 'weather_private')
worksheet_1 = spreadsheet.worksheet('2013')

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
