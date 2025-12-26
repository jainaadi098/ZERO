import time
import random
import pyttsx3  
import speech_recognition as sr 



engine = pyttsx3.init()

def speak(text):
    engine.setProperty('rate', 180)
    engine.say(text)
    engine.runAndWait()



def get_voice_input():
    """
    Listens to the microphone and returns the recognized text as a string.
    Returns None if the audio was not understood.
    """
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting for background noise... One second.")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
        print("Listening... Speak now!")
        try:
            # Set a timeout so it doesn't hang forever if no one speaks
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            print("Processing...")
            # Convert audio to text
            text = recognizer.recognize_google(audio)
            return text.lower()  # Return text in lowercase for easier comparison
            
        except sr.WaitTimeoutError:
            print("Error: No speech detected within the timeout.")
            return None
        except sr.UnknownValueError:
            print("Error: Could not understand the audio.")
            return None
        except sr.RequestError:
            print("Error: Could not reach the recognition service (Check Internet).")
            return None


print("Enter name")
speak("Enter name")
name=get_voice_input()
print(name)
speak(name)



def input_audio():
    print("In this game we will count the number from 1 \n And at the place of numbers multiple of 5 we count 0 ")
    print("Let start the game!")
    speak('''In this game we will count the number from 1 \n And at the place of numbers multiple of 5 we count 0 
          Let start the game!''')

def process(count,num):
    if (count+1)%5==0 and num==0:
        return True
    elif (count+1)%5!=0 and num==(count+1):
        return True
    else:
        return False

def play():
    player=1
    computer=2
    turn=random.randint(1,2)
    count=0
    while True:
        if turn==1:
            time.sleep(1)
            print("Player Turn")
            # num=int(input("Enter :"))
            num=get_voice_input()
            valid=process(count,num)
            if valid==False:
                
                break
            else:
                count+=1
                turn=2
        if turn==2:
            time.sleep(1)
            print("Computer Turn")
            if (count+1)%5==0:
                num=0
                count+=1
                
            else:
                num=count+1
                count+=1
            time.sleep(1.5)
            print(num)
            turn=1

play()
print("Game Over")