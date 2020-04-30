import requests

class Message:
    """This class will representate the received message
    from the API, it will get the message and it will
    have methods to get specifcs informations """

    def __init__(self, token):
        """Initialize the attributes of the message"""

        token = str(token)

        if self.check_connection(token):
            self._json = self.access_api(token).json()
        else:
            raise ValueError('Something went wrong')
      
    def __str__(self):
        """Represents the class like a string"""

        return self.format_json(self._json)

    @staticmethod
    def format_json(json):
        """Pretify the received json"""

        dictionary_json = json
        return """Cifrado: {}\n
        Decifrado: {}""". format(dictionary_json['cifrado'], dictionary_json['decifrado'])
                                

    @staticmethod
    def access_api(token):
        """This fuction will accessthe api returnning the reponse"""

        default_url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
        params ={'token': token}
        response = requests.get(default_url, params=params)

        return response

    
    def check_connection(self, token):
        """Checks if the connections was well succeed"""

        response = self.access_api(token)
        if response:
            return True 
        else:
            raise ValueError('Invalid Token or connection!!!')



