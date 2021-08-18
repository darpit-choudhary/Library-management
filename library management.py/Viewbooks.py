import tkinter as tk
import pymysql
import tkinter.messagebox as tmsg

    #connect to mysql
my_pass = "D@rpit123"
my_database = 'db'

con = pymysql.connect(host = 'localhost', user = 'root', password = my_pass, database = my_database)
cur = con.cursor()

table_of_books = "books"
    
def view():
    global root
    
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Book list")
    
    #canvs for background
    canvas1 = tk.Canvas(root)
    canvas1.config(bg = 'blue')
    canvas1.pack(expand = True, fill = 'both')
    
    #frame for headline and headline label
     # frame for headline
    f1 = tk.Frame(root)
    f1.place(relx = 0.35, rely = 0.15, relwidth = 0.35, relheight = 0.1)
    #head line label
    tk.Label(f1, text = 'Book list', font = 'lucida 15 italic', bg = 'black', fg = 'white').place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    
    f2 = tk.Frame(root, bg = 'black')
    f2.place(relx = 0.1, rely =0.35, relwidth = 0.8, relheight = 0.4)
    
    tk.Label(f2, text="%-10s%-40s%-30s%-20s"%('BID','Title','Author','Status'),
    bg='black',fg='white').place(relx=0.07,rely=0.1)
    tk.Label(f2, text = "----------------------------------------------------------------------------",bg='black',fg='white').place (relx=0.05,rely=0.2)
    
    get_book = "select * from "+table_of_books
    
    y=0.3
    
    try:
        cur.execute(get_book)
        con.commit()
        
        for i in cur:
            tk.Label(f2,text="%-10s%-40s%-30s%-20s"%(i[0],i[1],i[2],i[3]) ,bg='black', fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        tmsg.showinfo("Error", "There was some error")
        
    #quit
    tk.Button(root, text = "Quit", font = 'georgia 15', command = root.destroy).place(relx = 0.45, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    root.mainloop()