from tkinter import *
import keyboard
import time

window = Tk()
window.geometry("300x600")
window.resizable(False, False)
window.title("Spam Bot v1.1")

text = "Spam Bot v1.1"
def bas():
    x = 0
    y = int(kackre.get())
    z = float(kacms.get())
    t = float(kacms2.get())
    time.sleep(t)

    while x<y:
        keyboard.write(giris.get())
        time.sleep(z)
        keyboard.press_and_release('Enter')
        time.sleep(0.1)
        x += 1



def kapa():
    keyboard.press_and_release('alt + f4')

def max():
    window.geometry(newGeometry="1920x1080+0+0")

baslik = Label(window, text=text, font=("Bauhaus 93",25))
buton = Button(window, text="spam", font=("Colonna MT", 20),command=bas , height=10, width=10)
butonkapa = Button(window, text="⨉",font=("Arial", 15), command=kapa)
butonmax = Button(window, text="◻",font=("Arial", 15), command=max)
giris = Entry(window,  font=("Dubai", 10), background="red")
kackre = Entry(window, font=("Dubai", 10),background="blue")
kacms = Entry(window,  font=("Dubai", 10),background="green")
kacms2 = Entry(window,  font=("Dubai", 10),background="yellow")
info = Label(window, text="red: text, blue: repeat count\n green: spam cooldown, yellow: time to start", font=("Calibri", 10))


baslik.pack(pady=50)
buton.pack(pady=10)
butonkapa.place(x=10, y=10)
butonmax.place(x=50, y=10)
giris.pack()
kackre.pack()
kacms.pack()
kacms2.pack()
info.pack()


window.mainloop()
