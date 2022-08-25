import pygsheets
import numpy as np
from google.oauth2 import service_account


def print_sheet(estc_no, uuid):
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
        print(row[1])
        if row[1] == estc_no:
            print('found it at index', index)
            wks.update_value("S{}".format(index), uuid)
            break

    # Update a cell with value (just to let him know values is updated ;) )
    # wks.update_value('A1', "Hey yank this numpy array")
    # my_nparray = np.random.randint(10, size=(3, 4))

    # update the sheet with array
    # wks.update_values('A2', my_nparray.tolist())

    # share the sheet with your friend
    # sh.share("myFriend@gmail.com")
