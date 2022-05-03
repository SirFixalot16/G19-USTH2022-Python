from tkinter import*
import tkinter as tk
from tkinter import ttk

      
class MainApp(ttk.Frame):
    def something():
       root = Tk()
       root.title('Pick your desired seat')
       root.iconbitmap('plane.ico')
     
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.mainframe = ttk.Frame(self.parent)
        self.canvas = tk.Canvas(self.mainframe)
        self.frame = ttk.Frame(self.canvas)
        self.gen_layout()
        self.column_row_config()

    def column_row_config(self):
        self.parent.rowconfigure(0, weight=1)
        self.parent.columnconfigure(0, weight=1)

    def gen_layout(self):
        self.mainframe.grid(row=0, column=0, sticky='nsew')
        self.canvas.grid(row=0, column=0, sticky='nsew')
        self.frame.grid(row=0, column=0, sticky='nsew')
        self.make_seats()
        self.access_seat_numb(1)

    def make_seats(self):
        # create 100 buttons on 10 rows
        seat_counter = 1
        for x in range(10):
            for y in range(1, 11):
                # print('creating seat %d' % seat_counter)
                b = ttk.Button(
                    self.frame, text='Seat%d' % seat_counter,
                    name='seat%d' % seat_counter
                )
                # doesn't matter that the columns won't line up
                b.grid(row=x, column=y)
                seat_counter += 1

    def access_seat_numb(self, numb):
        # print(self.frame.children)
        for k, v in self.frame.children.items():
            if k == 'seat%d' % numb:
                # run some code on a seat numb
                print(v._name)

if __name__ == '__main__':
    root = tk.Tk()
    MainApp(root)
    root.mainloop()