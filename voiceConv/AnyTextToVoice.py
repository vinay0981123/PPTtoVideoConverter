from gtts import gTTS  
from time import sleep
from pygame import mixer
# This module is imported so that we can  
# play the converted audio  
  
# from playsound import playsound  

def mplayer(name): 
        '''  for playing music  '''
        mixer.init() 
        mixer.music.load(name)
        mixer.music.set_volume(0.7) 
        mixer.music.play()


def hindiToVoiceConvertor(textToConvert):
    text_val =  textToConvert
    # Here are converting in Hindi Language  
    language = 'hi'  
        
    # Passing the text and language to the engine,  
    # here we have assign slow=False. Which denotes  
    # the module that the transformed audio should  
    # have a high speed  
    obj = gTTS(text=text_val, lang=language, slow=False)  
        
    #Here we are saving the transformed audio in a mp3 file named  
    # exam.mp3  
    # os.remove('exam.mp3')
    # sleep(1)
    obj.save("Hindi.mp3")   
        
    
    filename='Hindi.mp3'
    mplayer(filename)

    while mixer.music.get_busy():
        
        # you may have to handle the events here 
        # pygame.event.pump()
        # [...]
        
        pass