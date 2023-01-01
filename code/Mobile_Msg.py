

import requests

class Message_mobile:
    def __init__(self,mobile,message,api_key):
        self.mobile=mobile
        self.message=message
        self.api_key=api_key
        pass
    def message_mobile(self):
        try:
            
            
            url = "https://api.sms-magic.com/v1/sms/send"
            payload = f"mobile_number={self.mobile}&sms_text={self.message}&sender_id=market"
            headers = {
                    'apiKey': f"{self.api_key}",
                    }
            
            response = requests.request("GET", url, headers=headers, params=payload)
            
            print(response.text)
            


        except:
            print("Error in mobile msg")
        return "Done Mobile Msg"



# a=Massage()
# print(a.massage_mobile())
