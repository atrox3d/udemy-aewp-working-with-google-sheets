import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet('weather_private')
worksheet_1 = spreadsheet.worksheet('2013')

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
# get row values
###########################################################
row = worksheet_1.row_values(6)
print(f'{row=}')
