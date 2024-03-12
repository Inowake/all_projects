from tkinter import *
import keyboard
import time

window = Tk()
window.geometry("300x600")
window.resizable(False, False)
window.title("Mal deronder")

text = "Spam Bot v1"
def bas():
    # text = "43"
    # metin.pack(side=BOTTOM)
    # buton.configure(text="mega zeki deren", font=("Cooper Black", 30))
    time.sleep(1)
    x = 0
    y = int(kackre.get())
    while x<y:
        keyboard.write(giris.get())
        time.sleep(0.2)
        keyboard.press_and_release('Enter')
        x += 1



def kapa():
    keyboard.press_and_release('alt + f4')

def max():
    window.geometry(newGeometry="1920x1080+0+0")

baslik = Label(window, text=text, font=("Bauhaus 93",25))
buton = Button(window, text="spamla", font=("Colonna MT", 20),command=bas , height=10, width=10)
metin = Label(window, text="muaaahhahahha")
butonkapa = Button(window, text="⨉",font=("Arial", 15), command=kapa)
butonmax = Button(window, text="◻",font=("Arial", 15), command=max)
giris = Entry(window, text="varsayılamayan metin", font=("Dubai", 10))
kackre = Entry(window, text="ne", font=("Dubai", 10),)

# baslik.place(x=0 ,y=0)
baslik.pack(pady=50)
buton.pack(pady=10)
butonkapa.place(x=10, y=10)
butonmax.place(x=50, y=10)
giris.pack()
kackre.pack()

window.mainloop()