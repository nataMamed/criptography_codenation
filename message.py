import requests
import json

class Message:
    """This class will representate the received message
    from the API, it will get the message and it will
    have methods to get specifcs informations """

    def __init__(self, token):
        """Initialize the attributes of the message"""

        token = str(token)

        if self.check_connection(token):
            self._json = self.access_api(token).json()
            self._json['decifrado'] = self.decipher()
            self.write_json()
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

    def write_json(self):
        """Write the file in a json format"""

        with open('answer.json', 'w') as file:
            json.dump(self._json, file)

    @staticmethod
    def load_json():
        """Read a json file"""

        with open('answer.json', 'r') as file:
            return json.load(file)

    def decipher(self):
        """Decipher the received message"""

        decipher_number = self._json['numero_casas']
        encrypted = self._json['cifrado'].split()
        decipher_message = self._json['decifrado']

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for word in encrypted:
            new_word = ''
            for letter in word:
                
                letter_position = alphabet.find(letter)
                new_letter_position =( letter_position - decipher_number)%26
                new_word = f'{new_word}{alphabet[new_letter_position]}'

            decipher_message = f"{decipher_message} {new_word}"

        return decipher_message
