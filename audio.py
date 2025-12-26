import pyttsx3 as tts  
import speech_recognition as sr 

# --- INITIALIZATION ---
engine = tts.init()
voices = engine.getProperty('voices')

# Set voice to index 1 (female usually) if available, otherwise use default (0)
if len(voices) > 1:
    engine.setProperty('voice', voices[1].id)
else:
    engine.setProperty('voice', voices[0].id)

def speak(text):
    """Speaks the text provided."""
    engine.say(text)
    engine.runAndWait()

def get_input(prompt_text):
    """
    Tries to get input via Microphone first.
    If that fails (timeout/error), falls back to Keyboard input.
    """
    print(f"\n🎧 {prompt_text}") 
    speak(prompt_text)

    # --- 1. TRY VOICE ---
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("   Adjusting noise... (Wait)")
            r.adjust_for_ambient_noise(source, duration=1)
            r.pause_threshold = 1
            
            print("   🎤 LISTENING NOW... (Speak!)")
            # Listening with timeout
            audio = r.listen(source, timeout=8, phrase_time_limit=5)
            
            print("   Processing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"   ✅ You said: {query}")
            return query.lower()

    # --- 2. IF VOICE FAILS -> TYPE ---
    except sr.WaitTimeoutError:
        print("   ❌ Timeout: No voice detected.")
        speak("I couldn't hear you. Please type it.")
    except sr.UnknownValueError:
        print("   ❌ Error: Could not understand audio.")
        speak("I didn't understand. Please type it.")
    except Exception as e:
        print(f"   ❌ Mic Error: {e}")
        speak("There was a microphone error. Please type it.")
    
    # Backup: Typing Input
    return input("   ⌨️  Please Type here: ").strip().lower()

# --- MAIN EXECUTION ---

# We call the function AND pass the prompt text here
name = get_input("Please enter your name")

# Confirming the result
print(f"\nFinal Result: {name}")
speak(f"Hello {name}")