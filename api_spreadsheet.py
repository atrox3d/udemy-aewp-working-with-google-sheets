def get_spreadsheet(spreadsheet_name):
    """ get spreadsheet """
    spreadsheet = gc.open(spreadsheet_name)
    return spreadsheet
