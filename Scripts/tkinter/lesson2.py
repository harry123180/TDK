import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
e = tk.Entry(window,show=None)
e.pack()
def inser_point():
    var = e.get()
    t.insert('insert',var)
    
def insert_end():
    var = e.get()
    t.insert('end',var)

bt1 = tk.Button(window,text = 'insert point ',width = 15, 
               height = 2 , command = inser_point)
bt1.pack()
bt2 = tk.Button(window,text = 'insert end',
                command = insert_end)
bt2.pack()
t = tk.Text(window,height = 2)
t.pack()
window.mainloop()