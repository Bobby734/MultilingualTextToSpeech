# This module is to accept text and convert to speech, using gTTS python module and utilizes langauges available for speech conversion.
import gtts
from gtts import gTTS
from io import BytesIO

# Creating list variables for langauges and their keys available with gTTS module.
lang_dict = gtts.lang.tts_langs()
lang_keys = list(lang_dict.keys())
lang_values = list(lang_dict.values())
position = lang_values.index("English")

# Defining a function to accept text and convert to BytesIO object.
def TextToSpeech(text : str, lang=lang_keys[position], fname='YourText'):

    if text:
        tts = gTTS(text, lang = lang)
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        return mp3_fp
    else:
        return f"Please provide valid text."
