
def close(session_attributes, fulfillment_state, message):
    response = {
        'sessionAttribute': session_attributes,
        'dialogAction': {
            'type': 'Close',
            'fulfillmentState': fulfillment_state,
            'message': message
        }
    }
    return response


def next_delegate(delegate):
    return {"dialogAction": {
        "type": "Delegate",
        "slots": {
            "testSlot": "US"
        }
    }}


def build_response(action, message):
    response = {"dialogAction": {
        "type": action,
        "fulfillmentState": "Fulfilled",
        "message": {
            "contentType": "PlainText",
            "content": message
        },
        "responseCard": {
            "version": 1,
            "contentType": "application/vnd.amazonaws.card.generic",
            "genericAttachments": [
                {
                    "title": "card-title",
                    "subTitle": "card-sub-title",
                    "imageUrl": "https://lh4.ggpht.com/mJDgTDUOtIyHcrb69WM0cpaxFwCNW6f0VQ2ExA7dMKpMDrZ0A6ta64OCX3H-NMdRd20=w300",
                    "attachmentLinkUrl": "https://lh4.ggpht.com/mJDgTDUOtIyHcrb69WM0cpaxFwCNW6f0VQ2ExA7dMKpMDrZ0A6ta64OCX3H-NMdRd20=w300",
                    "buttons": [
                        {
                            "text": "Lemon",
                            "value": "lemon"
                        },
                        {
                            "text": "Raspberry",
                            "value": "raspberry"
                        },
                        {
                            "text": "Plain",
                            "value": "plain"
                        }
                    ]
                }
            ]
        }
    }}
    return response


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message, response_card):
    return {
        'sessionAttributes': session_attributes,
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent_name,
            'slots': slots,
            'slotToElicit': slot_to_elicit,
            'message': message,
            'responseCard': response_card
        }
    }


def elicit_slot(intent, slots, elicitSlot, msg):
    return {
        'sessionAttributes': {},
        'dialogAction': {
            'type': 'ElicitSlot',
            'intentName': intent,
            'slots': slots,
            'slotToElicit': elicitSlot,
            'message': {'contentType': 'PlainText', 'content': msg}
        }
    }


def elicit_intent(msg="How can I help you?"):
    return {
        "sessionAttributes": {},
        "dialogAction": {
            "type": "ElicitIntent",
            "message": {
                "contentType": "PlainText",
                "content": msg
            }
        }
    }


def welcomeMessage(sessionAttribute):
    # print("Welcome message")
    # return elicit_intent("Hi..Are are interested in internship or fulltime opportunities?")
    return elicit_intent()

def getOpenPositions():
    positions = ['Software Engineer', 'Data Scientist', 'Data Analyst']
    # Code to fetch from data to get the open positions
    return positions


def getText():
    positions = getOpenPositions()
    text = ''
    idx = 1
    for job in positions:
        print("%s %s\n" % (idx, job))
        text += ("%s %s\n" % (idx, job))
        idx = idx+ 1

    return text


def lambda_handler(event, context):
    print("Lamda handler called()")
    print("Event %s "%(event))
    # print(getText(getOpenPositions()))
    # print("Session attributes User id : %s" % event["sessionAttributes"]["userId"])
    if event["currentIntent"]["name"] == "WelcomeMessage":
        user_name = event["sessionAttributes"]["userName"]
        company_name = event["sessionAttributes"]["compName"]
        return elicit_intent((
                             "Hello %s..Glad that you are interested in a career with %s. What kind of opportunities are you looking for - Internship / Fulltime?") % (
            user_name, company_name))
    elif event["currentIntent"]["name"] == "JobApplication":
        print("job application intent case")
        if not event["currentIntent"]["slots"]["Position"]:
            return elicit_slot("JobApplication", {"slots": event["currentIntent"]["slots"]}, "Position",
                               "which type of job are interested in?\n ")
        elif not event["currentIntent"]["slots"]["Month"]:
            return elicit_slot("JobApplication", {"slots": event["currentIntent"]["slots"]}, "Month",
                               "when are you available to start from?")
        else:
            return elicit_intent(("These are the position which are currently available:. \n %s" % (getText())))
    elif event["currentIntent"]["name"] == "GetJobFromList":
        if event["currentIntent"]["slots"]["Desingation"] != 'null':
            return elicit_slot("JobApplication", {"slots": event["currentIntent"]["slots"]}, "Desingation",
                               "Please mention above menioned positions")
        else:

            return build_response("Close", "Applied !!! Thanks for applying")
    else:
        return elicit_intent("Hi")
