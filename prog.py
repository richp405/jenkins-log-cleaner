#!/usr/local/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox as mb


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        # self.hi_there = tk.Button(self.master)
        # self.hi_there[
        #     "text"
        # ] = "Try2: First interactive input attempt\n-----------------------\n(click me)"
        # self.hi_there["command"] = self.say_hi
        # self.hi_there.grid(row=0, column=2)

        tk.Label(
            self.master,
            text="   Parse Jenkins Logfile Paragraphs   ",
            font=("Times New Roman", 26),
            background="blue",
            foreground="white",
            just="center",
        ).grid(row=2, column=1)

        tk.Label(
            self.master,
            text="Paste original -->",
            just="right",
        ).grid(row=4, column=0)

        self.entrythingy = ScrolledText(self.master, font=("Courier New", 16), height=4)
        self.entrythingy.insert(tk.INSERT, "Put log code here")
        self.entrythingy.grid(row=4, column=1, columnspan=3)

        self.output_thingy = ScrolledText(
            self.master, font=("Courier New", 18), height=24, width=110
        )
        self.output_thingy.insert(tk.INSERT, "Translation will show here...")
        self.output_thingy.grid(row=5, column=1, columnspan=4)

        self.myprocess = tk.Button(
            self.master,
            text=">> Process <<",
            pady=2,
            command=self.procdata,
        )
        self.myprocess.grid(row=8, column=1)

        self.quit = tk.Button(
            self.master,
            text="-  QUIT  -",
            command=self.validatequit,
            pady=2,
        )
        self.quit.grid(row=8, column=2)

    def say_hi(self):
        print("hi there, everyone!")

    def procdata(self):
        tv = self.entrythingy.get("1.0", tk.END)
        tv = tv.replace("\\n", "\n")
        tv = tv.replace("\\r", "")
        tv = tv.replace("\\\\", "\\")
        tv = tv.replace("\\\\", "\\")
        tv = tv.replace('\\"', '"')
        tv = tv.replace("\\'", "'")
        tv = tv.replace(', "', ',\n"')
        indent = 0
        row = 0
        inquote = 0
        indquote = 0
        tl = []
        tl.append("")
        for tc in tv:
            if tc != "\r" and (tc != "\n" or indquote):
                tl[row] += tc
            if tc == '"':
                indquote ^= 1
            if tc == "'":
                inquote ^= 1
            if indquote == 0:
                if tc == "\n" or tc == "\\":  # tc == "/" or
                    row += 1
                    tl.append("")
                    tl[row] = " " * indent
                if (
                    tc == "("
                    or tc == ")"
                    or tc == "["
                    or tc == "]"
                    or tc == "{"
                    or tc == "}"
                ):
                    row += 1
                    if tc == "(" or tc == "[" or tc == "{":
                        indent += 2
                    else:
                        indent -= 2
                    tl.append("")
                    tl[row] = " " * indent

        tv = "\n".join(tl)

        self.output_thingy.delete("1.0", tk.END)
        self.output_thingy.insert(tk.INSERT, tv)
        # mb.showinfo("Proc", tstr)
        # print(tstr)

    # def print_contents(self, event):
    # print("Hi. The current entry content is:", self.contents.get())

    def validatequit(self):
        if mb.askyesno("Quit?", "Do you want to exit?", icon="question", default="no"):
            self.master.destroy()


root = tk.Tk()
root.title("Getting more into tkinter")
root.geometry("1400x700")
app = Application(master=root)
app.mainloop()
