import requests
import json
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")


if __name__=='__main__':

    city = input("Enter the name of the city\n")

    url = f"https://api.weatherapi.com/v1/current.json?key=a9f2496c7b514c9c97393322231712&q={city}"

    r = requests.get(url)
    # print(r.text)
    wdict = json.loads(r.text)
    print(wdict["current"]["temp_c"])
    x=wdict["current"]["temp_c"]
    print(f"The current wheather of {city} is {x} degrees")
    w = f"The current wheather of {city} is {x} degrees"
    print(w)
    speak.speak(w)