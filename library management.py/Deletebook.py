import tkinter as tk
import pymysql
import tkinter.messagebox as tmsg

#connect to mysql server
my_pass = 'D@rpit123'
my_database = 'db'

con = pymysql.connect(host = 'localhost', user = 'root', password = my_pass, database = my_database)
cur = con.cursor()

table_of_books = 'Books'
issue_table = 'Books_issued'

def delete_book():
    
    bookid = book_id.get()
    
    deletesql = "delete from "+table_of_books+" where bid = '"+bookid+"'"
    deleteissue = "delete from "+issue_table+" where bid = '"+bookid+"'"
    
    try:
        cur.execute(deletesql)
        con.commit()
        cur.execute(deleteissue)
        con.commit()
        tmsg.showinfo("Delete", "The book was deleted successfully")
    except:
        tmsg.showerror("Error", "There was some error while deleting the book")
        
    print(bookid)
    book_id.delete(0, tk.END)
    root.destroy()


def delete():
    
    #define some global variables
    global root, book_id, con, cur, canvas1, title_of_books
    
    root = tk.Tk()
    root.title("Delete Book")
    root.geometry("600x500")
    
    #canvas for background
    canvas1 = tk.Canvas(root)
    canvas1.config(bg = 'red')
    canvas1.pack(expand = True, fill = 'both')
    
    
    # frame for headline
    f1 = tk.Frame(root)
    f1.place(relx = 0.35, rely = 0.15, relwidth = 0.35, relheight = 0.1)
    #head line label
    tk.Label(f1, text = 'Add book details', font = 'lucida 15 italic', bg = 'black', fg = 'white').place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    
    # frame for entries
    f2 = tk.Frame(root, bg = 'black')
    f2.place(relx = 0.1, rely =0.35, relwidth = 0.8, relheight = 0.4)
    
    # book id
    tk.Label(f2, text = 'Book Id :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.45, relheight = 0.1)
    book_id = tk.Entry(f2, font = 'georgia')
    book_id.place(relx = 0.4, rely = 0.45, relwidth = 0.5, relheight = 0.1)
    
    #submit
    tk.Button(root, text = "Submit", font = 'georgia 15', command = delete_book).place(relx = 0.1, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    #quit
    tk.Button(root, text = "Quit", font = 'georgia 15', command = root.destroy).place(relx = 0.7, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    root.mainloop()