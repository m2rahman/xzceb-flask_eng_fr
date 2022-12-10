"""all import here"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION="2022-12-05"

authenticator = IAMAuthenticator(apikey, disable_ssl_verification=True)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(url)

language_translator.set_disable_ssl_verification(True)

"""english to french function"""
def english_to_french(englishText):
    french_text = language_translator.translate(
    text=englishText,
    model_id='en-fr').get_result()
    return french_text

"""french to english function"""
def french_to_english(frenchText):
    english_text = language_translator.translate(
    text=frenchText,
    model_id='fr-en').get_result()
    return english_text
