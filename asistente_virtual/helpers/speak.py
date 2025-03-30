import pyttsx3




def speak(text):
    """Función para sintetizar texto a voz."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()