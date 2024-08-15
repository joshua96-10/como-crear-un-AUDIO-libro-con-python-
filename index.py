from  gtts  import gTTS

archivo = open("libro.txt", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()

tts = gTTS(text = texto, lang="es")
tts.save("audio-libro.mp3")
