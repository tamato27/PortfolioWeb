

def check_valid_client(rec_json_data):
    """ Checks for valid client from db and return true or false """

    # Temp db setup
    db = {"CLIENT_ID": "1",
          "CLIENT_NAME": "RSA",
          "CLIENT_API_TOKEN": "a1623e5ed0402a2b6ee15315fb16e5111097c6a77a52abf59a26beca4db61960",
          "NO_OF_QR_CODES": "2"}

    # Check if api key is valid
    rec_client_name_val = rec_json_data['client']["client_name"]
    rec_db_key_val = rec_json_data['client']["api_token"]
    print(rec_client_name_val)

    # get id of company from db
    db_client_id = db['CLIENT_ID']
    db_client_name = db['CLIENT_NAME']
    # if id matches company name then co_id = CLIENT_ID

    # Validate client
    if rec_json_data:
        # Check client name and client id in database
        if rec_json_data['client']['client_name'] in db_client_name and rec_json_data['client']['client_id'] in db['CLIENT_ID']:
            print(f"Valid ClientName: {rec_client_name_val}")
            if rec_json_data['client']["api_token"] == db['CLIENT_API_TOKEN']:
                print(f"Valid API Token You may proceed:{rec_json_data['client']['api_token']}")

                # Setup Email
                user_email = f"{rec_json_data['username'].lower()}.{rec_json_data['surname'].lower()}{rec_json_data['domain']}"
                user_email = user_email.replace(" ", "")  # remove all white spaces

                # Build the Dict for use of API
                client_dict = {"username": rec_json_data['username'],
                               "surname": rec_json_data['surname'],
                               "mobile_phone": rec_json_data['mobile_phone'],
                               "job_title": rec_json_data['job_title'],
                               "department": rec_json_data['department'],
                               "business_unit": rec_json_data['business_unit'],
                               "email": user_email
                               }

                try:
                    print(client_dict)
                    return client_dict
                except NameError as error:
                    print("The Dictionary is empty! because of invalid values", error)
                    error_description = "The Dictionary is empty! because of invalid values"
                    return error_description

            else:
                print("The User and/or id was incorrect You may not proceed")
                error_description = "The User and/or token was incorrect You may not proceed"
                return error_description
        else:
            print("Not a valid Company!")
            error_description = "Not a valid Company!"
            return error_description


def validate_client(rec_json_data):
    """ Validate clients for use of API """
    # Temp db setup
    db = {"CLIENT_ID": "1",
          "CLIENT_NAME": "RSA",
          "CLIENT_API_TOKEN": "a1623e5ed0402a2b6ee15315fb16e5111097c6a77a52abf59a26beca4db61960",
          "NO_OF_QR_CODES": "2"}

    # Check if api key is valid
    rec_client_name_val = rec_json_data['ACLIENT']["client_name"]
    rec_db_key_val = rec_json_data['ACLIENT']["api_token"]
    print(rec_client_name_val)

    # get id of company from db
    db_client_id = db['CLIENT_ID']
    db_client_name = db['CLIENT_NAME']
    # if id matches company name then co_id = CLIENT_ID

    # Validate client
    if rec_json_data:
        # Check client name and client id in database
        if rec_json_data['ACLIENT']['client_name'] in db_client_name and rec_json_data['ACLIENT']['client_id'] in db['CLIENT_ID']:
            print(f"Valid ClientName: {rec_client_name_val}")
            if rec_json_data['ACLIENT']["api_token"] == db['CLIENT_API_TOKEN']:
                print(f"Valid API Token You may proceed:{rec_json_data['ACLIENT']['api_token']}")
                return True

                try:
                    print(client_dict)
                    return client_dict
                except NameError as error:
                    print("The Dictionary is empty! because of invalid values", error)
                    error_description = "The Dictionary is empty! because of invalid values"
                    return error_description

            else:
                print("The User and/or id was incorrect You may not proceed")
                error_description = "The User and/or token was incorrect You may not proceed"
                return error_description
        else:
            print("Not a valid Company!")
            error_description = "Not a valid Company!"
            return error_description


def json_email():
    pass


def qr_vcard(client):
    """ Generate a qr vcard and return """

    return client


def qr_std():
    pass
