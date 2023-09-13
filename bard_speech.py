import speech_recognition as sr
from bardapi import BardCookies
import datetime

# Create a recognizer instance
recognizer = sr.Recognizer()

# Define your BardCookies instance and cookie_dict as before
cookie_dict = {
    "__Secure-1PSID": "aQjAPfgN-1oOhvAp_-L9NeXXrpqN8v82Ef9UIUup4Xi5vPPeQm25zqdTaFP2q9odGWHL7w.",
    "__Secure-1PSIDTS": "sidts-CjEBSAxbGf9l8QPSXCh8ltuUsWi-GQrk9xtuBinKioJJWhWPSEAsqSpgpJw33XhBzUNIEAA",
    "__Secure-1PSIDCC": "APoG2W8v46N93fmXELDFPLEF6n79tfjBcXKOAPDs_DeZdShZeWsD7id1iPwLbdiBksQsesGsBg"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    try:
        # Use microphone as the audio source
        with sr.Microphone() as source:
            print("Say something...")
            # Listen to the user's speech and recognize it
            audio = recognizer.listen(source)

        # Convert the recognized speech to text
        query = recognizer.recognize_google(audio)

        # Get an answer from Bard API based on the recognized query
        reply = bard.get_answer(query)['content']

        # Print the reply
        print("You said: " + query)
        print("Bard's reply: " + reply)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("An error occurred: {0}".format(e))