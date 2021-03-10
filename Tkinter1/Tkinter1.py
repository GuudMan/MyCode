import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('500x300')

# tk中的字符串变量
var = tk.StringVar()

l = tk.Label(window, textvariable=var, bg='green',
             font=('Arial', 12), width=15, height=2)
l.pack()
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        var.set("you hit me")
        on_hit = True
    else:
        on_hit = False
        var.set("")


b = tk.Button(window, text="hit me", width=15, height=2,
              command=hit_me)
b.pack()
window.mainloop()