import tkinter as tk
from tkinter import *


class MainWindow:
    def __init__(self):
        self.running = False
        self.window = Tk()

        self.window.title("Timer")
        self.window.geometry('250x150')

        self.frame = tk.Frame(
            padx=1,
            pady=1,
            borderwidth=1,
            relief=SOLID
        )
        self.frame.pack(fill = BOTH)

        self.lbl = tk.Label(
            self.frame,
            text="00:00:00"
        )
        self.lbl.pack()

        self.btn = tk.Button(
            self.frame,
            text="Start",
            command=self.click_button1
        )
        self.btn.pack()

        self.frame2 = tk.Frame(
            padx=1,
            pady=10,
            borderwidth=1,
            relief=SOLID
        )
        self.frame2.pack(fill = BOTH)

        self.entry1 = tk.Entry(
            self.frame2
        )
        self.entry1.insert(0, 0)
        self.entry1.pack(anchor = "n")

        self.entry2 = tk.Entry(
            self.frame2
        )
        self.entry2.insert(0, 0)
        self.entry2.pack(anchor = "n")

        self.entry3 = tk.Entry(
            self.frame2
        )
        self.entry3.insert(0, 0)
        self.entry3.pack(anchor = "n")

        self.btn2 = tk.Button(
            self.frame2,
            text="Start",
            command = self.click_button2
        )
        self.btn2.pack()

        self.window.mainloop()

    def click_button1(self):
        self.time = 0
        if not self.running:
            self.running = True
            self.update_time1()
        else:
            self.running = False
            self.update_time1()

    def update_time1(self):
        if self.running:
            self.time += 1
            self.lbl.config(text=self.time_convert(self.time))
            self.window.after(2, self.update_time1)


    def click_button2(self):
        self.time1 = int(self.entry1.get())
        self.time2 = int(self.entry2.get())
        self.time3 = int(self.entry3.get())
        if not self.running:
            self.running = True
            self.update_time2()
        else:
            self.running = False
            self.update_time2()

    def update_time2(self):
        if self.running:
            if self.time1 != 0:
                self.time1 -= 1
                self.entry1.delete(0, tk.END)
                self.entry1.insert(0, str(self.time1))
                self.window.after(1000, self.update_time2)
            else:
                self.update_time3()
                self.time1 = 60


    def update_time3(self):
        if self.running:
            if self.time2 != 0:
                self.time2 -= 1
                self.entry2.delete(0, tk.END)
                self.entry2.insert(0, str(self.time2))
                self.window.after(1000, self.update_time2)
            else:
                self.update_time4()
                self.time2 = 60

    def update_time4(self):
        if self.running:
            self.time3 -= 1
            self.entry3.delete(0, tk.END)
            self.entry3.insert(0, str(self.time3))
            self.window.after(1000, self.update_time3)

    def time_convert(self, time):
        self.hours = time // 3600
        self.minutes = (time % 3600) // 60
        self.seconds = time % 60
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

app = MainWindow()