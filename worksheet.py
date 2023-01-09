import api_connection
import api_spreadsheet

gc = api_connection.get_connection('secret/google-drive-api.json')
spreadsheet = api_spreadsheet.get_spreadsheet('weather_private')


if __name__ == '__main__':
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
