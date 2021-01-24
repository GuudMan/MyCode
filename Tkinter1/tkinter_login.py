import pickle
import tkinter as tk
import tkinter.messagebox

window = tk.Tk()
window.title("Welcome to ZTE")
window.geometry('450x300')

# welcom image
canvas = tk.Canvas(window, height=200, width=300)
image_file = tk.PhotoImage(file='welcome.gif')
image=canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

#user infomation
tk.Label(window, text='User name').place(x=50, y=150)
tk.Label(window, text='User name').place(x=50, y=190)

var_usr_name = tk.StringVar()
# 设置默认值
var_usr_name.set('example@python.com')
var_usr_pwd = tk.StringVar()
# 文本框
entry_user_name = tk.Entry(window, textvariable=var_usr_name)
entry_user_name.place(x=160, y=150)

entry_user_passwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_user_passwd.place(x=160, y=190)


def usr_login():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usrs_info.pickle', 'rb') as usr_file:
            usrs_info = pickle.load(usr_file)
    except FileNotFoundError:
        with open('usrs_info.pickle', 'wb') as usr_file:
            usrs_info = {'admin': 'admin'}
            pickle.dump(usrs_info, usr_file)

        if usr_name in usrs_info:
            if usr_pwd == usrs_info[usr_name]:
                tk.messagebox.showinfo(title='welcome', message='how are you'+usr_name)
            else:
                tk.messagebox.showerror(title='Error', message='your passwd is wrong')
        else:
            is_sign_up = tk.messagebox.askyesno(message='welcome'+usr_name+'you have not sign would want to sign')
            if is_sign_up:
                usr_sign_up()


def usr_sign_up():
    pass


#login button
btn_login = tk.Button(window, text='login', command=usr_login).place(x=170, y=230)
btn_sign_up = tk.Button(window, text='sign up', command=usr_sign_up).place(x=270, y=230)



window.mainloop()