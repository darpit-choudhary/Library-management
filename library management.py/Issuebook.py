import tkinter as tk
import pymysql
import tkinter.messagebox as tmsg

#connect to mysql server
my_pass = 'root'          #example password
my_database = 'db'

con = pymysql.connect(host = 'localhost', user = 'root', password = my_pass, database = my_database)
cur = con.cursor()

issue_table = "Books_issued"
table_of_books = 'Books'

#list of all book ids
list_bookid = list()

def issue_book():
    global availability, book_id, issue_name
    
    bookid = book_id.get()
    issueto = issue_name.get()
    
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
                
                if check == 'available':
                    availability = True
                else:
                    availability = False
        else:
            tmsg.showerror("Error", "Book ID does not exist")
    except:
        tmsg.showerror("Error", "Can't get book data")
    
    issuesql = "insert into "+issue_table+" values('"+bookid+"','"+issueto+"')"
    show = "select * from "+issue_table
    update_status = "update "+table_of_books+" set availability = 'issued' where bid = '"+bookid+"'"
    
    try:
        if bookid in list_bookid and availability == True:
            cur.execute(issuesql)
            con.commit()
            cur.execute(update_status)
            con.commit()
            tmsg.showinfo("Success", "The book was issued")
            root.destroy()
        else:
            list_bookid.clear()
            tmsg.showerror("Error", "Book already issued")
            root.destroy()
            return
    except:
        tmsg.showerror("Search error", "The ID enterd was wrong, Try again")
    
    print(bookid)
    print(issueto)
    
    list_bookid.clear()
    


def issue():
    
    #define some global variables
    global root, book_id, issue_name, availability, canvas1
    
    root = tk.Tk()
    root.title("Issue Book")
    root.geometry("600x500")
    
    #canvas for background
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
    tk.Label(f2, text = 'Book Id :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.35, relheight = 0.1)
    book_id = tk.Entry(f2, font = 'georgia')
    book_id.place(relx = 0.4, rely = 0.35, relwidth = 0.5, relheight = 0.1)
    
    #issued to
    tk.Label(f2, text = 'Issued to :', font = 'georgia 15', bg = 'black', fg = 'white').place(relx = 0.05, rely = 0.55, relheight = 0.1)
    issue_name = tk.Entry(f2, font = 'georgia')
    issue_name.place(relx = 0.4, rely = 0.55, relwidth = 0.5, relheight = 0.1)
    
    #submit
    tk.Button(root, text = "Submit", font = 'georgia 15', command = issue_book).place(relx = 0.1, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    #quit
    tk.Button(root, text = "Quit", font = 'georgia 15', command = root.destroy).place(relx = 0.7, rely = 0.85, relwidth = 0.2, relheight = 0.08)
    
    root.mainloop()
