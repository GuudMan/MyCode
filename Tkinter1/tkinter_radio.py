import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

var = tk.StringVar()

# t=tk.Text(window,height=2,bg='red')
# t.pack()
l = tk.Label(window, width=20, bg='green', text='empty')
l.pack()


def print_selection():
    l.config(text='you have selected ' + var.get())


r1 = tk.Radiobutton(window, text='option A',
                    variable=var, value='A',
                    command=print_selection)
r1.pack()

r2 = tk.Radiobutton(window, text='option B',
                    variable=var, value='B',
                    command=print_selection)
r2.pack()
r3 = tk.Radiobutton(window, text='option C',
                    variable=var, value='C',
                    command=print_selection)
r3.pack()
window.mainloop()