import tkinter as tk

root = tk.Tk()


def callback():
    print("~被调用啦~")


# 创建一个顶级菜单
menubar = tk.Menu(root)
menubar.add_command(label="Hello", command=callback)
menubar.add_command(label="Quit", command=root.quit)

# 显示菜单
root.config(menu=menubar)

root.mainloop()