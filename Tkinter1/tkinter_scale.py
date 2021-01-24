import tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')



# t=tk.Text(window,height=2,bg='red')
# t.pack()
l = tk.Label(window, width=20, bg='green', text='empty')
l.pack()


def print_selection(v):
    l.config(text='you have selected ' + v)


s=tk.Scale(window, label='try me', from_=5, to=11, orient=tk.HORIZONTAL,
           length=200, showvalue=1, tickinterval=2,
           resolution=0.1, command=print_selection)# 保留两位小数0.1
s.pack()
window.mainloop()