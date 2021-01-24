import tkinter as tk

window=tk.Tk()
window.title("my window frame")
window.geometry('200x200')
tk.Label(window, text='on the window').pack()

frame=tk.Frame(window).pack()
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')
tk.Label(frame_l, text='on the frame_l1').pack()
tk.Label(frame_l, text='on the frame_l2').pack()
tk.Label(frame_r, text='on the frame_r1').pack()


window.mainloop()