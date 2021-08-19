import tkinter as tk
from PIL import Image, ImageTk
import pymysql
from Addbook import *
from Deletebook import *
from Issuebook import *
from Returnbook import *
from Viewbooks import *

root = tk.Tk()
root.geometry("600x500")
root.title("Library Management")
root.wm_iconbitmap("Library_books.ico")
#root.attributes('-fullscreen', True)

#connect to mysql
my_pass = 'root' #password example
my_database = 'db'   #database name

con = pymysql.connect(host = 'localhost', user = 'root', password = my_pass, database = my_database)
cur = con.cursor()

# TODO background image

background_image =Image.open("Library 2.jpg")
[newimageSizeWidth, newimageSizeHeight] = background_image.size

background_image = background_image.resize((newimageSizeWidth,newimageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)
Canvas1 = tk.Canvas(root)
Canvas1.create_image(300,340,image = img)      
Canvas1.config(bg="white",width = newimageSizeWidth, height = newimageSizeHeight)
Canvas1.pack(expand=True,fill='both')

# heading frame and heading label
f1 = tk.Frame(root, borderwidth = 5, bg = 'red')
f1.place(relx = 0.25, rely = 0.1, relwidth = 0.5, relheight = 0.2)
heading_label = tk.Label(f1, text = "Welcome to \n My Library", bg = 'black', font = 'courier 15 bold', fg = 'white')
heading_label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

#button options
lst_buttons = ['View book list', 'Add book', 'Delete Book', 'Issue Book', 'Return Book']

b = tk.Button(root, text = lst_buttons[0], bg = 'black', command = view, fg = 'white', font = 'georgia 15')
b.place(relx = 0.32, rely = 0.4, relwidth = 0.35, relheight = 0.1)

b = tk.Button(root, text = lst_buttons[1], command = add, bg = 'black', fg = 'white', font = 'georgia 15')
b.place(relx = 0.32, rely = 0.5, relwidth = 0.35, relheight = 0.1)

b = tk.Button(root, text = lst_buttons[2], command = delete, bg = 'black', fg = 'white', font = 'georgia 15')
b.place(relx = 0.32, rely = 0.6, relwidth = 0.35, relheight = 0.1)

b = tk.Button(root, text = lst_buttons[3], bg = 'black', fg = 'white', command = issue, font = 'georgia 15')
b.place(relx = 0.32, rely = 0.7, relwidth = 0.35, relheight = 0.1)

b = tk.Button(root, text = lst_buttons[4], bg = 'black', fg = 'white', command = return_book, font = 'georgia 15')
b.place(relx = 0.32, rely = 0.8, relwidth = 0.35, relheight = 0.1)
    
root.mainloop()
