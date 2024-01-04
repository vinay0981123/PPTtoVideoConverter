from googletrans import Translator
from englisttohindi.englisttohindi import EngtoHindi
from AnyTextToVoice import hindiToVoiceConvertor
# importing the module
# from englisttohindi.englisttohindi import EngtoHindi
def translatorText(message):
    # message.replace('\n',"")
    get_sentence=str(message)
    get_sentence=get_sentence.replace('\n',"")
    print(f"message is: {get_sentence}")
    # s=s.lower()
    # print(f"message is {s}")
    # res = EngtoHindi(s)
    # # displaying the translation
    # print(res.convert)
    # get_sentence='Lets talk about gatling. So Gatling is a highly capable load testing tool. It is designed for ease of use, maintainability and high performance. Out of the box, Gatling comes with excellent support of the HTTP protocol that makes it a tool of choice for load testing any HTTP server. This is written in Scala JVM compatible Embedded DSL for testing Easy to use Light.'
    translator = Translator()
        
    # short form of english in which
    # you will speak
    from_lang = 'en'
        
    # In which we want to convert, short
    # form of hindi
    to_lang = 'hi'
    text_to_translate = translator.translate(get_sentence,src= from_lang,dest= to_lang)
    # Storing the translated text in text
    # variable
    text = text_to_translate.text
    print(f"translation is: {text}")
    hindiToVoiceConvertor(text)


