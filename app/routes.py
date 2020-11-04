import africastalking
#from flask import render_template
from flask import request
#from flask import url_for
import pandas as pd
import csv

from app import app



username = "sandbox"
api_key = "7f5e92258234b42b32233f706b654afdcbc2e1fc6dc911c16a191efd59c8657c"
africastalking.initialize(username, api_key)
sms = africastalking.SMS


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    sms_phone_number = []
    sms_phone_number.append(phone_number)

    ussd_split = text.split('*')
    level = len(ussd_split)

    if text == "":
        # main menu
        response = "CON Welcome to SICLife Insurance\n"
        response += "1. New Client\n"
        response += "2. Existing Policy holder\n"
        #response += "3. Send me a cool message"
    elif text == "1":
        # sub menu 1
        file=pd.read_csv('/home/theprince/myUSSD/policy.csv')
        #with open('/home/theprince/myUSSD/policy.csv', newline='') as csvfile:
            #file = list(csv.reader(csvfile, delimiter=' ', quotechar='|'))
            #for row in file:
                #val=file[0][0]

        val=file['name']
        response = "CON Select your product type for payment\n"
        response += val
        #response += "1. G Plan"
        #response += "2. Education Plan Plus"
        #response += "3. Funeral Policy"
        #response += "4. Sika Plan"
    elif text == "2":
        # sub menu 1
        response = "END Your phone number is {}".format(phone_number)
    #elif text == "3":
    #    try:
            # sending the sms
    #        sms_response = sms.send("Thank you for going through this tutorial", sms_phone_number)
    #        print(sms_response)
    #    except Exception as e:
            # show us what went wrong
    #        print(f"Houston, we have a problem: {e}")
    elif text == "1*1":

        response="CON Please enter your full name:\n"
        # ussd menus are split using *
        #account_number = "1243324376742"
        #response = "END Your account number is {}".format(account_number)
    elif ussd_split[0]=="1" and ussd_split[1]=="1" and level==3:


        response = "CON Select premium\n"
        response += "1. GHS50\n"
        response += "2. GHS100\n"
    elif ussd_split[0]=="1" and ussd_split[1]=="1" and level==4:
        c=ussd_split[1]
        d=""
        if ussd_split[2]=="1":
            d="GHS50"
        else:
            d="GHS100"

        response = "END Thank you\n"
        response += "Name: {}".format(c) + "\n"
        response += "Premium: {}".format(d)
    elif text == "1*2":
        response="END Please enter your full name:\n"
        #account_balance = "100,000"
        #response = "END Your account balance is USD {}".format(account_balance)
    else:
        response = "END Invalid input. Try again."

    return response



