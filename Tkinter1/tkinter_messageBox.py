import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')


def hit_me():
    # tk.messagebox.showinfo(title='Hi', message='hahahha')
    # tk.messagebox.showwarning(title='Hi', message='hahahha')
    # tk.messagebox.showerror(title='Hi', message='hahahha')
    # res = tk.messagebox.askquestion(title='Hi', message='hahahha') # return yes or no
    # print(res)
    # rest = tk.messagebox.askyesno(title='hi', message='hahahh') # return True or false
    # print(rest)
    rest = tk.messagebox.askokcancel('title', message='hhhhh')


button = tk.Button(window, text='hit me', command=hit_me).pack()

window.mainloop()