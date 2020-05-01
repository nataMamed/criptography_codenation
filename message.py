import requests
import json
import hashlib


class Message:
    """This class will representate the received message
    from the API, it will get the message and it will
    have methods to get specifcs informations """

    def __init__(self, token):
        """Initialize the attributes of the message"""

        token = str(token)

        if self.check_connection(token):
            self._json = self.access_api(token).json()
            self.write_json()
        else:
            raise ValueError('Something went wrong')
      
    def __str__(self):
        """Represents the class like a string"""

        encrypted = self._json['cifrado']
        decipher = self._json['decifrado']
        return f"Encrypted: {encrypted} \n Decipher: {decipher}"
    
    def format_json(self):
        """Pretify the received json"""

        self._json['decifrado'] = self.decipher()
        self._json['cifrado'] = self._json['cifrado'].lower()
        self._json['resumo_criptografico'] = self.create_sha1()

    @staticmethod
    def access_api(token):
        """This fuction will accessthe api returnning the reponse"""

        get_url = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data'
        params ={'token': token}
        response = requests.get(get_url, params=params)

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

        self.format_json()

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
        encrypted = self._json['cifrado'].lower().split()
        decipher_message = (self._json['decifrado'])

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        for word in encrypted:
            new_word = ''

            for letter in word:
                if letter in alphabet:
                    
                    letter_position = alphabet.find(letter)
                    new_letter_position =( letter_position - decipher_number)%26
                    new_word = new_word + alphabet[new_letter_position]

                else:
                    new_word = new_word + letter


            decipher_message = f"{decipher_message} {new_word}"
                

        return decipher_message
    
    def create_sha1(self):

        """Use the sha1 algorithm to encrypt the 
        decifer message"""

        decipher = self._json['decifrado']
        result = hashlib.sha1(decipher.encode())
        summary = result.hexdigest()

        return summary

    @staticmethod
    def send_answer(token):
        """Send the file as a multipart/form-data like
        a HTML formulary"""

        params = {'token': str(token)}
        post_url = 'https://api.codenation.dev/v1/challenge/dev-ps/submit-solution'

        answer = {'answer': open('answer.json', 'rb')}
        
        response = requests.post(post_url, files=answer, params=params)

        return response