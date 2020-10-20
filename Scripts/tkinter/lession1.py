import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')
var = tk.StringVar()

l = tk.Label(window,textvariable = var,font=('Arial',12),width = 15
             ,height = 2,bg = 'red')

l.pack()
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('測試')
    else:
        on_hit = False
        var.set('')
bt = tk.Button(window,text = '測試 ',width = 15,
               height = 2 , command = hit_me)

bt.pack()

window.mainloop()