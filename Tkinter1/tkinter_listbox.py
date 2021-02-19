import  tkinter as tk

window = tk.Tk()
window.title("my window")
window.geometry('200x200')

var1 = tk.StringVar()
l = tk.Label(window, bg="red", height=2, width=15, textvariable=var1)
l.pack()


def print_selected():
    value = lb.get(lb.curselection())
    var1.set(value)


t = tk.Text(window, height=2)
t.pack
b = tk.Button(window, text="print selected", width=15, height=2, command=print_selected)
b.pack()

var2 = tk.StringVar()
var2.set(('lrc', 'lq', 'yt', 'lzx'))
lb = tk.Listbox(window, listvariable=var2)
list_item = [1, 2, 3, 4]
for item in list_item:
    lb.insert('end',item)
lb.insert(1, 'first')
lb.insert(2, 'second')
lb.delete(2)
lb.pack()
window.mainloop()