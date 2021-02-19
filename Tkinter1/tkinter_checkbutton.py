import tkinter as tk

window = tk.Tk()
window.title("my window!")
window.geometry('200x200')
l = tk.Label(window, height=2, bg='yellow', text='empty')
l.pack()


def print_selection():
    if (var1.get() == 1) & (var2.get() == 0):
        l.config(text='you only love python')
    elif (var1.get() == 0) & (var2.get() == 1):
        l.config(text='you only love c++')
    elif (var1.get() == 0) & (var2.get() == 0):
        l.config(text='you love either')
    else:
        l.config(text='you love both')


var1 = tk.IntVar()
var2 = tk.IntVar()
cb1 = tk.Checkbutton(window, text='python', variable=var1, onvalue=1,
                     offvalue=0, command=print_selection)
cb1.pack()
cb2 = tk.Checkbutton(window, text='c++', variable=var2, onvalue=1,
                     offvalue=0, command=print_selection)

cb2.pack()
window.mainloop()