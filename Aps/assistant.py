import speech_recognition as sr
import pyttsx3
import datetime

audio = sr.Recognizer()
machine = pyttsx3.init()

machine.say("Olá, sou a Nix. Como posso ajudar?")
machine.runAndWait()

def execute_command():
    try:
        with sr.Microphone() as source:
            print("Captado")
            voice = audio.listen(source)
            command = audio.recognize_google(voice, language="pt-BR")
            command = command.lower()
            if "nix" in command:
                command = command.replace("nix", "")
                machine.say("Você disse: " + command)
                machine.runAndWait()
            return command
    except sr.UnknownValueError:
        print("Não consegui entender o que você disse. Tente novamente.")
        return ""
    except sr.RequestError as e:
        print(f"Erro ao conectar ao serviço de reconhecimento: {e}")
        return ""
    except Exception as e:
        print(f"Um erro inesperado ocorreu: {e}")
        return ""

def command_voice_user():
    command = execute_command()
    if "horas" in command:
        hour = datetime.datetime.now().strftime("%H:%M")
        machine.say("Agora são " + hour)
        machine.runAndWait()

command_voice_user()
