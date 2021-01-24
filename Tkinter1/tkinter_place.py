import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 放置方式1
# tk.Label(window, text=1).pack(side='left')
# tk.Label(window, text=1).pack(side='right')
# tk.Label(window, text=1).pack(side='bottom')
# tk.Label(window, text=1).pack(side='top')

# 放置方式2
# for i in range(4):
#     for j in range(3):
#         tk.Label(window, text=i+j).grid(row=i, column=j, padx=10, pady=10)# padx、pady设置行间距

# 放置方式3
tk.Label(window, text=1).place(x=10, y=100, anchor='nw')

window.mainloop()