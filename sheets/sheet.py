import pygsheets
from google.oauth2 import service_account


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'client_secret.json'
GOOGLE_SHEET_KEY='1YkFjV5lNwjC5ZPDrxux0ylUKis8q9ux1Vlydehmmzn4'


def _get_sheet():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    gc = pygsheets.authorize(custom_credentials=credentials)

    # Open spreadsheet and then worksheet
    # open sheet - https://docs.google.com/spreadsheets/d/1YkFjV5lNwjC5ZPDrxux0ylUKis8q9ux1Vlydehmmzn4/edit?pli=1#gid=0
    sh = gc.open_by_key(GOOGLE_SHEET_KEY)
    return sh


def update_uuid_in_sheet_for_estc_number(estc_no, uuid):
    sh = _get_sheet()
    wks = sh.worksheet_by_title('Pipeline Progress')
    index = 0
    for row in wks:
        index += 1
        if row[1] == estc_no:
            print('found given ESTC number at index', index)
            wks.update_value("S{}".format(index), uuid)
            break


def get_full_printer_name_for_short_name(printer_short_name):
    sh = _get_sheet()
    wks = sh.worksheet_by_title('Printers')
    index = 0
    for row in wks:
        index += 1
        if row[1] == printer_short_name:
            print('Found printer full name for short name', printer_short_name, row[0])
            return row[0]
    print("Could not find printer full name for short name - ", printer_short_name)
    return printer_short_name
