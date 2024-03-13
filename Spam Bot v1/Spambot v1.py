from tkinter import *
import keyboard
import time

window = Tk()
window.geometry("300x375")
# window.resizable(False, False)
window.title("Spam Bot v1.1r")
window.config(bg="grey10")

text = "Spam Bot v1.1r"
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
    keyboard.press_and_release('win + up')

def mini():
    keyboard.press_and_release('win + down')

baslik = Label(window, text=text, font=("Bauhaus 93",25), fg="white", bg="grey10")
buton = Button(window, text="spam", font=("Bauhaus 93", 15),command=bas , height=1, width=10, background="grey30", fg="white")
butonkapa = Button(window, text="⨉",font=("Arial", 15,), command=kapa, height=1, width=2, background="grey30", fg="white")
butonmax = Button(window, text="◻",font=("Arial", 15), command=max, height=1, width=2, background="grey30", fg="white")
butonmin = Button(window, text="–",font=("Arial", 15), command=mini, height=1, width=2, background="grey30", fg="white")
giris = Entry(window,  font=("Dubai", 10), width=40, borderwidth="3", background="red")
kackre = Entry(window, font=("Dubai", 10), width=40, borderwidth="3",background="blue")
kacms = Entry(window,  font=("Dubai", 10), width=40, borderwidth="3",background="green")
kacms2 = Entry(window,  font=("Dubai", 10), width=40, borderwidth="3",background="yellow")
info = Label(window, text="red: text, blue: repeat count\n green: spam cooldown, yellow: time to start", font=("Calibri", 10),bg="grey10",fg="white")


baslik.pack(pady=50)

butonkapa.place(x=90, y=10)
butonmax.place(x=130, y=10)
butonmin.place(x=170, y=10)
giris.pack()
kackre.pack()
kacms.pack()
kacms2.pack()
buton.pack(pady=10)
info.pack()


window.mainloop()
