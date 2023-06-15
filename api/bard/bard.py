import bardapi
import os

class Bard():
    def __init__(self, input_text):
        os.environ['_BARD_API_KEY'] = 'WwhgnwX5QtrnLMhhPxuTOytu2bzZwZRyxoJsIa6uoG8kedYITApdXCNMXcPm-NfLqGTlmQ.'
        response = self.get_text(input_text=input_text)


    def get_text(self, input_text):
        response = bardapi.core.Bard().get_answer(input_test)


def Bard_api(input_text: str):

    input_test = input_text
    response = bardapi.core.Bard().get_answer(input_test)

    return response