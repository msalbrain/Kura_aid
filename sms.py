from __future__ import print_function

import africastalking


class SMS:
    def __init__(self):
        # Set your app credentials
        self.username = 'sandbox'

        self.api_key = '2a76a4abc3474a10602399e4d173dae474604380e10b1169ba92f44f4ff98571'


        # Initialize the SDK
        africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
        self.sms = africastalking.SMS


    def send(self):
        # Set the numbers you want to send to in international format
        recipients = ["+2349070899078"]

        # Set your message
        message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

        # Set your shortCode or senderId
        sender = "93453"
        try:
            # Thats it, hit send and we'll take care of the rest.
            response = self.sms.send(message, recipients, sender)
            print(response)
        except Exception as e:
            print('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()
