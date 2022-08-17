from tkinter import *


# -*- coding:utf-8 -*-

def btn_clicked():
    stringG.set('')
    stringH.set('')
    stringR.set('')


def action():
    gender = stringG.get()
    height = float(stringH.get())

    if gender == 'Мужской' or gender == 'мужской':
        stringR.set(round(52 + 1.9 * (height / 2.54 - 60), 1))
    elif gender == 'Женский' or gender == 'женский':
        stringR.set(round(49 + 1.7 * (height / 2.54 - 60), 1))
    else:
        stringG.set('Неверный ввод')


path = 'C:/Users/Erina/file_code/Tkinter_figma/generated_code'

window = Tk()

stringG = StringVar()
stringH = StringVar()
stringR = StringVar()

window.title("Perfect Weight")
window.geometry("360x775")
window.configure(bg="#b291c7")
canvas = Canvas(
    window,
    bg="#b291c7",
    height=775,
    width=360,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

entry0_img = PhotoImage(file=f"img_textBox0.png")
entry0_bg = canvas.create_image(
    187.5, 503.5,
    image=entry0_img)

entry0 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    textvariable=stringR)

entry0.place(
    x=151, y=489,
    width=73,
    height=27)

entry1_img = PhotoImage(file=f"img_textBox1.png")
entry1_bg = canvas.create_image(
    184.5, 327.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    textvariable=stringH)

entry1.place(
    x=81.5, y=306,
    width=206.0,
    height=41)

entry2_img = PhotoImage(file=f"img_textBox2.png")
entry2_bg = canvas.create_image(
    179.5, 218.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    bg="#d9d9d9",
    highlightthickness=0,
    textvariable=stringG)

entry2.place(
    x=76.5, y=197,
    width=206.0,
    height=41)

img0 = PhotoImage(file=f"img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=action,
    relief="flat")

b0.place(
    x=79, y=690,
    width=212,
    height=65)

background_img = PhotoImage(file=f"background.png")
background = canvas.create_image(
    180.0, 353.0,
    image=background_img)

window.resizable(False, False)
window.mainloop()
