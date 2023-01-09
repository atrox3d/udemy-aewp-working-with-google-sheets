import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet('weather_private')
worksheet_1 = spreadsheet.worksheet('2013')
ws1 = worksheet_1

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
