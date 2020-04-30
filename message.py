import requests

class Message:
    """This class will representate the received message
    from the API, it will get the message and it will
    have methods to get specifcs informations """

    def __init__(self, token):
        """Initialize the attributes of the message"""


    def access_api(self, token):
        """This fuction will accessthe api returnning the reponse"""

        default_url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
        params ={'token': str(token)}
        response = requests.get(default_url, params=params)

        return response

    @staticmethod
    def check_connection(response):
        """Checks if the connections was well succeed"""

        if response:
            return True 
        else:
            raise ValueError('Invalid Token!!!')



