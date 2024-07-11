# import win32com.client as wincom
# import time
# speak = wincom.Dispatch("SAPI.SpVoice")
# time.sleep(-2)
# text = "Python text-to-speech test. using win32com.client"
# speak.Speak(text)
# time.sleep(12)


import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
if __name__=='__main__':
    print("welcome to Robo speaker 1.1 created by Harry")
    while True:
        x = input("Enter what you want to speak:\n")
        if x == 'quit':
            break
        speak.speak(x)