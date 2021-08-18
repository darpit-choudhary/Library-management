import tkinter as tk
import pymysql
import tkinter.messagebox as tmsg

#connect to mysql server
my_pass = 'D@rpit123'
my_database = 'db'

con = pymysql.connect(host = 'localhost', user = 'root', password = my_pass, database = my_database)
cur = con.cursor()

#title of book list
table_of_books = "Books"

def register():
    
    title = book_title.get()
    bookid = book_id.get()
    author = author_name.get()
    availability = status.get()
    availability = availability.lower()
    
    insert_books = "insert into "+table_of_books+" values('"+bookid+"','"+title+"','"+author+"','"+availability+"')"
    
    try:
        cur.execute(insert_books)
        con.commit()
        tmsg.showinfo("Succes", "Book added successfully")
    except:
        tmsg.showerror("Error", "There was some error while adding the book")
        
    print(title)
    print(bookid)
    print(author)
    print(availability)
    
    root.destroy()

def add():
    
    #define some golbal variables
    global root,book_id,book_title,author_name,status,canvas1,con,cur,table_of_books
    
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Add Book")
    
    #make a canvas for background
    canvas1 = tk.Canvas(root)
    canvas1.config(bg = 'green')
    canvas1.pack(fill = 'both', expand = True)
    
    
    # frame for headline
    f1 = tk.Frame(root)
    f1.place(relx = 0.35, rely = 0.15, relwidth = 0.35, relheight = 0.1)
    #head line label
    tk.Label(f1, text = 'Add book details', font = 'lucida 15 italic', bg = 'black', fg = 'white').place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    
    # frame for entries
    f2 = tk.Frame(root, bg = 'black')
    f2.place(relx = 0.1, rely =0.35, relwidth = 0.8, relheight = 0.4)
    
    # book id
    tk.Label(f2, text = 'Book Id :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.15, relheight = 0.1)
    book_id = tk.Entry(f2, font = 'georgia')
    book_id.place(relx = 0.4, rely = 0.15, relwidth = 0.5, relheight = 0.1)
    
    # book title
    tk.Label(f2, text = 'Book name :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.35, relheight = 0.1)
    book_title = tk.Entry(f2, font = 'georgia')
    book_title.place(relx = 0.4, rely = 0.35, relwidth = 0.5, relheight = 0.1)
    
    # author name
    tk.Label(f2, text = 'Author name :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.55,relheight = 0.1)
    author_name = tk.Entry(f2, font = 'georgia')
    author_name.place(relx = 0.4, rely = 0.55, relwidth = 0.5, relheight = 0.1)
    
    # status
    tk.Label(f2, text = 'Status :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.75, relheight = 0.1)
    status = tk.Entry(f2, font = 'georgia')
    status.place(relx = 0.4, rely = 0.75, relwidth = 0.5, relheight = 0.1)
    
    #submit
    tk.Button(root, text = "Submit", font = 'georgia 15', command = register).place(relx = 0.1, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    #quit
    tk.Button(root, text = "Quit", font = 'georgia 15', command = root.destroy).place(relx = 0.7, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    root.mainloop()