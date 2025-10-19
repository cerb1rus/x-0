from tkinter import *
window = Tk()
a = [8, 9, 10,
     7, 6, 5,
     2, 3, 4] #список, в котором будут сохраняться значения крестиков и ноликов

n = 1 #переменная, по которой мы определяем чей сейчас ход (Х = 1, 0 = 0)

window.geometry("380x450")
window.title("Крестики-нолики")
window.resizable(width=False, height=False)

label = Label(text="Сейчас ход Х!",
              font=("OCR A Extended", 25, "bold"))
label.place(x=55, y=20)

def restart_window(): #функция, реализующая перезапуск программы
    global a
    global n
    for i in btn:
         i.config(text="")
         i.config(state="active")
    a = [8, 9, 10,
         7, 6, 5,
         2, 3, 4]
    n = 1
    label.config(text="Сейчас ход X!")
    but_restart.place_forget()

def test(): #функция, реализующая три исхода игры
    if a[0] == a[1] == a[2] == 1 or a[3] == a[4] == a[5] == 1 or a[6] == a[7] == a[8] == 1 or a[0] == a[3] == a[6] == 1 or a[1] == a[4] == a[7] == 1 or a[2] == a[5] == a[8] == 1 or a[0] == a[4] == a[8] == 1 or a[2] == a[4] == a[6] == 1:
        but_restart.place(x=310, y=20)
        label.config(text="X выйграли!")
        for i in btn:
            i.config(state="disabled")

    elif a[0] == a[1] == a[2] == 0 or a[3] == a[4] == a[5] == 0 or a[6] == a[7] == a[8] == 0 or a[0] == a[3] == a[6] == 0 or a[1] == a[4] == a[7] == 0 or a[2] == a[5] == a[8] == 0 or a[0] == a[4] == a[8] == 0 or a[2] == a[4] == a[6] == 0:
        but_restart.place(x=310, y=20)
        label.config(text="0 выйграли!")
        for i in btn:
            i.config(state="disabled")

    elif set(a) == {0, 1}:
        label.config(text="   Ничья!")
        but_restart.place(x=310, y=20)

def button_clicked(k): #основная функция игры
    global n

    if n == 1: #ход крестика
        btn[k].config(text="X")
        label.config(text="Сейчас ход 0!")
        btn[k].config(state="disabled")
        a[k] = 1
        n = 0
        test()

    else: #ход нолика
        btn[k].config(text="0")
        label.config(text="Сейчас ход X!")
        btn[k].config(state="disabled")
        a[k] = 0
        n = 1
        test()

#кнопочки
but = Button(window, width=10, height=5, command=lambda: button_clicked(0))
but1 = Button(window, width=10, height=5, command=lambda: button_clicked(1))
but2 = Button(window, width=10, height=5, command=lambda: button_clicked(2))
but3 = Button(window, width=10, height=5, command=lambda: button_clicked(3))
but4 = Button(window, width=10, height=5, command=lambda: button_clicked(4))
but5 = Button(window, width=10, height=5, command=lambda: button_clicked(5))
but6 = Button(window, width=10, height=5, command=lambda: button_clicked(6))
but7 = Button(window, width=10, height=5, command=lambda: button_clicked(7))
but8 = Button(window, width=10, height=5, command=lambda: button_clicked(8))
btn = [but, but1, but2, but3, but4, but5, but6, but7, but8]

but.place(x=50, y=100)
but1.place(x=150, y=100)
but2.place(x=250, y=100)
but3.place(x=50, y=200)
but4.place(x=150, y=200)
but5.place(x=250, y=200)
but6.place(x=50, y=300)
but7.place(x=150, y=300)
but8.place(x=250, y=300)

but_restart = Button(window, width=6, height=3, command=restart_window, text="заново")
window.mainloop()