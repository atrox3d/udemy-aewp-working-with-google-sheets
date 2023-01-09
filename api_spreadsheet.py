def get_spreadsheet(gc, spreadsheet_name):
    """ get spreadsheet """
    spreadsheet = gc.open(spreadsheet_name)
    return spreadsheet
