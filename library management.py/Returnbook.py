import tkinter as tk
import pymysql
import tkinter.messagebox as tmsg

#connect to mysql 
my_pass = 'D@rpit123'
my_database = 'db'

con = pymysql.connect(host = 'localhost', user = 'root', password = my_pass, database = my_database)
cur = con.cursor()

table_of_books = "Books"
issue_table = "Books_issued"

list_bookid = list()
def submit_book():
    global availability, book_id
    
    bookid = book_id.get()
    extract_bookid = "select bid from "+table_of_books
    try:
        cur.execute(extract_bookid)
        con.commit()
        for i in cur:
            list_bookid.append(i[0])
            
        if bookid in list_bookid:
            check_status = "select availability from "+table_of_books+" where bid = '"+bookid+"'"
            cur.execute(check_status)
            con.commit()
            for i in cur:
                check = i[0]
            
                if check == 'issued':
                    availability = True
                else:
                    availability = False
        else:
            tmsg.showerror("Error", "Book ID does not exist")
    except:
        tmsg.showerror("Error", "Can't get book data")
            
    issuesql = "delete from "+issue_table+" where bid = '"+bookid+"'"
    print(bookid in list_bookid)
    print(availability)
    update_status = "update "+table_of_books+" set availability = 'available' where bid = '"+bookid+"'"
    
    try:
        if bookid in list_bookid and availability == True:
            cur.execute(issuesql)
            con.commit()
            cur.execute(update_status)
            con.commit()
            tmsg.showinfo("Success", "Book returned successfully")
        else:
            list_bookid.clear()
            tmsg.showerror("Error", "Book ID not correct, Try again")
            root.destroy()
            return
    except:
        tmsg.showerror("Error", "The ID entered is wrong , Try again")
    
    list_bookid.clear()
    root.destroy()


def return_book():
    
    #define some global variables
    global root, book_id, canvas1, availability
    
    root = tk.Tk()
    root.title("Return Book")
    root.geometry("600x500")
    
    #canvas for backgroun
    canvas1 = tk.Canvas(root)
    canvas1.config(bg = 'yellow')
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
    tk.Button(root, text = "Submit", font = 'georgia 15', command = submit_book).place(relx = 0.1, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    #quit
    tk.Button(root, text = "Quit", font = 'georgia 15', command = root.destroy).place(relx = 0.7, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    root.mainloop()