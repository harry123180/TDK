try:
    import Tkinter as tk
    from PIL import ImageTk, Image
except:
    import tkinter as tk
    from PIL import ImageTk, Image


class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x1000')
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="哈囉，歡迎光臨", font=('Helvetica', 40, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="請選主餐", font=('Helvetica', 20, "bold"),
                  command=lambda: master.switch_frame(PageOne)).pack(side = "bottom" ,fill="x", pady=5)



class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green')
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\car_view\\rice.png"))
        tk.Label(self, text="白飯",font=('Helvetica', 16, "bold")).grid(row=0,column=0)#pack(side="top", fill="x", pady=5)
        tk.Label(self,image = self.img).grid(row=10,column=0)

        tk.Label(self, text="粥", font=('Helvetica', 16, "bold")).grid(row=20,column=0)
        tk.Button(self, text="下一頁",
                  command=lambda: master.switch_frame(PageTwo)).grid(row=30,column=0)


class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\car_view\\food.jpg"))
        tk.Label(self, text="請將餐點放置框內", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, image=self.img).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="辨識中，請稍後...", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        tk.Button(self, text="下一頁",
                  command=lambda: master.switch_frame(PageThree)).pack()
class PageThree(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='green')
        tk.Label(self, text="主餐", font=('Helvetica', 25, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="飯....10元/碗", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="配菜", font=('Helvetica', 25, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="高麗菜 10元", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="杏胞菇  5元", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="蛋    10元", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="番茄   10元", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="茄子    5元", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="總金額:   50 元", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="下一頁",
                  command=lambda: master.switch_frame( PageFour)).pack()

class PageFour(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="SUE食.自助餐", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)

        tk.Button(self, text="現金支付",
                command=lambda: master.switch_frame(PageFive)).pack()
        tk.Button(self, text="電子支付",
                  command=lambda: master.switch_frame(PageSix)).pack()
        tk.Button(self, text="上一頁，確認價錢",
                  command=lambda: master.switch_frame(PageThree)).pack()
        tk.Label(self, text="謝謝光臨", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
class PageFive(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="請請取出票券", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="列印中，請稍後...", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="上一頁",
                  command=lambda: master.switch_frame(PageFour)).pack()
        tk.Button(self, text="出現問題?",
                  command=lambda: master.switch_frame(PageSeven)).pack()
class PageSix(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="請下方條碼讀取", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\Desktop\\car_view\\line code.jpg"))
        tk.Label(self, image=self.img).pack(side="top", fill="x", pady=5)
        tk.Label(self, text="結帳中，請稍後...", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="上一頁",
                  command=lambda: master.switch_frame(PageFour)).pack()
        tk.Button(self, text="出現問題?",
                  command=lambda: master.switch_frame(PageSeven)).pack()
class PageSeven(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self, bg='red')
        tk.Label(self, text="已呼叫服務人員，請稍後...", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="後台選項",
                  command=lambda: master.switch_frame(PageFour)).pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()