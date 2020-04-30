import requests

class Message:
    """This class will representate the received message
    from the API, it will get the message and it will
    have methods to get specifcs informations """

    def __init__(self):
        pass


    def access_api(self, token):
        """This fuction will accessthe api returnning the json"""

        default_url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
        params ={'token': str(token)}

        response = requests.get(default_url, params=params)

        json = response.json()
        return json

