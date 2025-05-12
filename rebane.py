import win32com.client

# Crear instancia del motor de voz
speaker = win32com.client.Dispatch("SAPI.SpVoice")

# (Opcional) Establecer una voz en español si está disponible
for voice in speaker.GetVoices():
    if "Spanish" in voice.GetDescription():
        speaker.Voice = voice
        break

# Frase a decir
text = "Jorge cállate"

# Reproducir la frase
speaker.Speak(text)
