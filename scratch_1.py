import tkinter as tk
import tkinter.font as tkfont
from PIL import ImageTk, Image
import matplotlib as plt
import array as arr


class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, bg='black')
        self.grid()
        self.createwidgets()

    def scrollhandler(self, *L):
        op, howMany = L[0], L[1]
        if op == 'scroll':
            units = L[2]
            self.entry.xview_scroll(howMany, units)
        elif op == 'moveto':
            self.entry.xview_moveto(howMany)

    def cleartext(self):
        self.entry.delete(0, 'end')
        return

    def click(self):
        workingNum = self.entry.get
        collatz_conjecture(workingNum)

    def createwidgets(self):
        centurygoth36 = tkfont.Font(family="Century Gothic", size=12, weight="bold")
        top = self.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.img = Image.open(r"C:\Users\witha\OneDrive\Desktop\Github_Projects\Python_Programming\Collatz Conjecture\labelheader.png")
        reduce_image = self.img.resize((600, 200), Image.ANTIALIAS)
        self.smaller_img = ImageTk.PhotoImage(reduce_image)
        imageLabel= tk.Label(self, image=self.smaller_img, anchor='center')
        imageLabel.grid(row=0, column=0, columnspan=4)
        self.entry = tk.Entry(self, width=30)
        self.entry.grid(row=6)
        self.entryScroll = tk.Scrollbar(orient=tk.HORIZONTAL, command=self.scrollhandler)
        self.entry['xscrollcommand'] = self.entryScroll.set
        numlabel = tk.Label(self, text='What number would you like to test?', fg='green', bg='black')
        numlabel.grid(row=6, column=0, stick=tk.W)
        self.showButton = tk.Button(self, text='Calculate', command=self.click, bg='green', fg='white')
        self.showButton.grid(row=6, sticky=tk.E)
        self.showButton['font'] = centurygoth36
        self.tryagainButton = tk.Button(self, text='Try Again!', width=20, command=self.cleartext, bg='green', fg='white')
        maxilabel = tk.Label(self, text='Max number reach:', fg='green', bg='black')
        maxilabel.grid(row=8, column=0, stick=tk.W)
        iterationlabel = tk.Label(self, text='How many steps did it take to reach 1:', fg='green', bg='black')
        iterationlabel.grid(row=9, column=0, stick=tk.W)
        self.tryagainButton.grid(row=11,column=0, sticky=tk.W)
        self.tryagainButton['font'] = centurygoth36
        self.quitButton = tk.Button(self, text='Quit', width=20, command=self.quit, bg='green', fg='white')
        self.quitButton.grid(row=11)
        self.quitButton['font'] = centurygoth36


def collatz_conjecture(base_num):
    number_array = arr.array('L')
    hailstone = base_num
    number_array.append(hailstone)
    while hailstone != 1:
        if hailstone % 2 != 0:
            hailstone = (3 * hailstone) + 1
            number_array.append(hailstone)
        else:
            hailstone = hailstone // 2
            number_array.append(hailstone)

    return number_array



def main():
    app = Application()
    app.master.title('Collatz Conjecture Tool')
    app['bg'] = 'black'
    app.mainloop()


if __name__ == '__main__':
    main()


