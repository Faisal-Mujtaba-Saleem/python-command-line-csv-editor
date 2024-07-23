import win32com.client as client
from pynput import keyboard
import speech_recognition as sr


def speak(text, dots=True):
    if dots:
        print(f'\n{text} ...')
    else:
        print(f'\n{text}')

    speaker = client.Dispatch('SAPI.SpVoice')
    speaker.Rate = -1
    speaker.speak(text)


user_typing = False


def handle_on_press(key):
    try:
        global user_typing
        if hasattr(key, 'name') and key.name == 'shift':
            user_typing = True
            speak('Switching to typing mode')
            return False  # Stop listener after first key press

    except Exception as e:
        speak(str(e))


def recognize_speech_from_microphone(prompt_text):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as the source of input
    with sr.Microphone() as source:
        try:
            # Initializing gobal variable user_typing
            global user_typing

            # Adjust the recognizer sensitivity to ambient noise and record audio. It listen for the short-period of time (secs) using microphone to take a sample of ambient-voice and adjusts the energy threshold/range of ambient noise to distinguish b/w the actual & ambient-voice.
            recognizer.adjust_for_ambient_noise(source)

            speak(f"{prompt_text}")

            # Wrap the audio listener within the keyboard listener so that if the user types on the keyboard while the audio listener is active, it will detect the key press and invoke the on_ handler. This handler will set the global variable user_typing to True. Using this variable, we can conditionally detect if the user is trying to type on the keyboard. All keyboard listening activities will occur on a separate thread.

            # Initializing keboard listner
            keyboard_listner = keyboard.Listener(on_press=handle_on_press)
            # Start to lisening
            keyboard_listner.start()

            # starts listening regularly for actual-voice.
            audio = recognizer.listen(source, timeout=10)

            # Stop lisening
            keyboard_listner.stop()

            if user_typing == True:
                user_typing = False
                speak('Switched. Please enter')
                return input()

            # Recognize speech using Google Web Speech API and convert it into the text.
            spoken_text = recognizer.recognize_google(audio)
            print(f'{spoken_text}')

            return spoken_text
        except Exception as e:
            speak(f'Sorry, I couldn\'t recognize your voice')
            if str(e) != '':
                print(str(e))
            return recognize_speech_from_microphone('Say again')


# Call the function to recognize speech
if __name__ == "__main__":
    recognized_text = recognize_speech_from_microphone()
    sample_text = 'Hi, How are you!'
    speak(sample_text)
