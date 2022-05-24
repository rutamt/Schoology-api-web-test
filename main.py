import schoolopy
import webbrowser as wb
import config
import time
import datetime
import os

def get_assignments(key, secret):

    config.name = None
    bl1 = "5167125116"
    bl2 = "5167125194"

    # This key can't really do anything, so it should be fine to leave here.


    # auth = schoolopy.Auth(key, secret, three_legged=True, domain=DOMAIN)
    # # Request authorization URL to open in another window.
    #
    # url = auth.request_authorization()
    #
    # # Open OAuth authorization webpage. Give time to authorize.
    # if url is not None:
    #     wb.open(url, new=2)
    #
    #
    # # Wait for user to accept or deny the request.
    # time.sleep(10)
    # # Authorize the Auth instance as the user has either accepted or not accepted the request.
    # # Returns False if failed.
    #
    # if not auth.authorize():
    #     raise SystemExit('Account was not authorized.')

    # Create a Schoology instance with Auth as a parameter.

    sc = schoolopy.Schoology(schoolopy.Auth(key, secret))

    # sc.limit = 10  # Only retrieve 10 objects max

    my_name = str(sc.get_me().name_display).split()[0]
    config.name = my_name
    assignments = sc.get_assignments(bl1) + sc.get_assignments(bl2)



    return assignments