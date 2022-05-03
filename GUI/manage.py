from tkinter import*
import random
import os


def __information__():
       filename = 'Customer_info_FrontEnd.py'
       os.system(filename)
       os.system('notepad'+filename)

def __FeeReport__():
       filename = 'Fee_Frontend.py'
       os.system(filename)
       os.system('notepad'+filename)
       
       
def menu():
       root = Tk()
       root.title('Airline booking management system')
       root.iconbitmap('plane.ico')
       root.geometry('1300x750')
       
       title_Frame = LabelFrame(root, font = ('arial',50,'bold'), width = 500, height = 100, bg = 'lightblue', relief = 'raise', bd = 13)
       title_Frame.grid(row = 0, column = 0, pady = 50)
       
       title_Label = Label(title_Frame, text = 'Airline booking Management System', font = ('arial',30,'bold'), bg = 'lightblue')
       title_Label.grid(row = 0, column = 0, padx = 150)


       #____FRAMES_______
       Frame_1 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 10)
       Frame_1.grid(row = 1, column = 0, padx = 300, pady = 7)
       Frame_2 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 10)
       Frame_2.grid(row = 2, column = 0, padx = 250, pady = 7)
       Frame_3 = LabelFrame(root, font = ('arial',17,'bold'), width = 1000, height = 100, bg = 'lightblue', relief = 'ridge', bd = 10)
       Frame_3.grid(row = 3, column = 0, padx = 280, pady = 7)


       #_____LABELS______
       Label_1 = Label(Frame_1, text = 'CUSTOMER PROFILE', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_1.grid(row = 0, column = 0, padx = 50, pady = 5)
       Label_2 = Label(Frame_2, text = 'PLANE INFORMATION ', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_2.grid(row = 0, column = 0, padx = 100, pady = 5)
       Label_3 = Label(Frame_3, text = 'FLIGHT DETAILS', font = ('arial',25,'bold'), bg = 'lightblue')
       Label_3.grid(row = 0, column = 0, padx = 100, pady = 5)
       
       


      #______BUTTON_____
       Button_1 = Button(Frame_1, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __information__)
       Button_1.grid(row = 0, column = 3, padx = 50)
       Button_2 = Button(Frame_2, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __FeeReport__)
       Button_2.grid(row = 0, column = 3, padx = 50)
       Button_3 = Button(Frame_3, text = 'VIEW', font = ('arial',16,'bold'), width = 8, command = __FeeReport__)
       Button_3.grid(row = 0, column = 3, padx = 50)


       

       root.mainloop()


       
       
if __name__ == '__main__':
       menu()
