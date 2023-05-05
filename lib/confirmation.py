import vonage
import os
from dotenv import load_dotenv



class SendConfirmation:
    def __init__(self,number, voonage=None):
        '''
        Parameters:
            number: String the required phone number to which a message should be sent
        returns:
            nothing        
        '''
        self.number = number
        self.voonage = voonage
    def send_confirmation_sms(self):
        '''
        Parameters:
            Nothing
        Returns:
            "Sent" if message was sent successfully
            "Not sent" if otherwise
        SideEffects:
            sent message using the Vonage API        
        '''
        if self.voonage is None:
            load_dotenv()
            client = vonage.Client(key=os.environ.get("API_KEY"),
                            secret=os.environ.get("SECRET"))
            self.voonage = vonage

            sms = vonage.Sms(client)
            responseData = sms.send_message(
                {
                    "from": "Vonage APIs",
                    "to":self.number,
                    "text": "Thank you! Your order was placed and will be delivered before 18:52"
                }
            )
        else:
            self.voonage = self.voonage

        #sms = self.vonage.Sms(client)        
            responseData = self.voonage.sms.send_message(
                {
                    "from": "Vonage APIs",
                    "to":self.number,
                    "text": "Thank you! Your order was placed and will be delivered before 18:52"
                }
            )
        if responseData["messages"][0]["status"] == "0":
            print("Message sent successfully.")
            return "Sent"
        else:
            print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
            return "Not sent"