import gspread
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
sa = gspread.service_account(filename="hh-project-395018-970a1c84a040.json")
 
def get_sheet_date():
    #helping-hands@hh-project-395018.iam.gserviceaccount.com
    #https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys?authuser=1&_gl=1*4fxxr0*_ga*MTU0NTc2NzY5NS4xNjkxMjU4Njk3*_ga_WH2QY8WWF5*MTY5MTI1ODY5Ny4xLjEuMTY5MTI1OTExNi4wLjAuMA..&_ga=2.113271495.-1545767695.1691258697&_gac=1.185789147.1691258905.CjwKCAjw5remBhBiEiwAxL2M92Q6IG4M1z7M5wIEPhtvK3C9a8_Cpjqq5tQ1QCQ39DVUTMN-R2Mq-hoChxoQAvD_BwE

    
    # received_sheet = sa.open("HH Receiving Form (Responses)")
    received_sheet = sa.open("HH Receiving Form (Responses)")
    received_worksheet = received_sheet.worksheet("Received")
    # delivered_sheet = sa.open("HH Delivery Form (Responses)")
    delivered_sheet = sa.open("HH Delivery Form (Responses)")
    delivered_worksheet = delivered_sheet.worksheet("Delivered")

    return {
        'received':received_worksheet.get_all_records(),
        'delivered':delivered_worksheet.get_all_records()
    }

@app.route('/')
@cross_origin()
def hello_world():
    return get_sheet_date()

if __name__ == '__main__':
    app.run()