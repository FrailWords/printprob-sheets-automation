import pygsheets
import numpy as np
from google.oauth2 import service_account


def update_uuid_in_sheet_for_estc_number(estc_no, uuid):
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'client_secret.json'

    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    gc = pygsheets.authorize(custom_credentials=credentials)

    # Open spreadsheet and then worksheet
    # open sheet - https://docs.google.com/spreadsheets/d/1YkFjV5lNwjC5ZPDrxux0ylUKis8q9ux1Vlydehmmzn4/edit?pli=1#gid=0
    sh = gc.open_by_key('1YkFjV5lNwjC5ZPDrxux0ylUKis8q9ux1Vlydehmmzn4')
    wks = sh.worksheet_by_title('Pipeline Progress')
    index = 0
    for row in wks:
        index += 1
        if row[1] == estc_no:
            print('found given ESTC number at index', index)
            wks.update_value("S{}".format(index), uuid)
            break
