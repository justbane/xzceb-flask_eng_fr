""" Translator module """
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)
language_translator.set_disable_ssl_verification(True)

# languages = language_translator.list_languages().get_result()
# print(json.dumps(languages, indent=2))

def english_to_french(english_text):
    """ Translator english to french """
    if english_text is not None:
        french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    return None

def french_to_english(french_text):
    """ Trnslatoe french to english """
    if french_text is not None:
        english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    return None
