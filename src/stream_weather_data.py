from time import sleep
import push_data_to_google_sheet as pdtgs

while True:
    service = pdtgs.setup_API()
    body = pdtgs.get_data_for_gsheet()
    pdtgs.write_data_to_gsheet(service, body)
    del body
    del service
    sleep(5)
 