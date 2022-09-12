import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

translator = Translator()

def clear():
    T2.delete(1.0, "end-1c")

def translate(text):
    clear()
    try:
        translation = translator.translate(text, dest='id')
        T2.insert(tk.END, translation.text)
    except:
        T2.insert(tk.END, "Tidak ada koneksi")




root = tk.Tk()
root.title("Translate")
root.geometry("500x250")


T1 = tk.Text(root, height=5, width=250)
T2 = tk.Text(root, height=5, width=250)
b = tk.Button(root, text='Translate', command= lambda: translate(T1.get(1.0, "end-1c")))
T1.pack()
b.pack()
T2.pack()

root.mainloop()
