import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('500x300')
text=tk.Label(window,text='Hello tkinter!',bg='yellow',width = 20).pack()

window.mainloop()