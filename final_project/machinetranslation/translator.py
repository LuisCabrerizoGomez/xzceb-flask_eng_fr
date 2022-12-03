""" Contains functions that allow us to translate from english to french and viceversa  """
import os

from dotenv import load_dotenv
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import LanguageTranslatorV3


def englishToFrench(english_text):
    """
    Function that allow us to translate a text from english to french
    """
    french_text = None
    if english_text is not None:
        response = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

        if len(response['translations']) > 0:
            french_text = response['translations'][0]['translation']
        else:
            french_text = ""

    return french_text

def frenchToEnglish(french_text):
    """
    Function that allow us to translate a text from french to english
    """
    english_text = None
    if french_text is not None:
        response = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

        if len(response['translations']) > 0:
            english_text = response['translations'][0]['translation']
        else:
            english_text = ""

    return english_text

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
