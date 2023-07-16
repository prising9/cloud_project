'''
Module to translate french to english and viceversa
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english):
    ''' Convert english text to french'''
    french = MyMemoryTranslator(source='english', target='french').translate(english)
    #print(frenchText)
    return french

def french_to_english(french):
    '''COnvert french to english API'''
    english = MyMemoryTranslator(source='french', target='english').translate(french)
    #print(englishText)
    return english

#englishToFrench("Hello, how are you?")
