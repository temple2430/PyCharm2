from tkinter import *
import sqlite3

root = Tk()
conn = sqlite3.connect('address_book.db')
cur = conn.cursor()

#cur.execute("""CREATE TABLE addresses(
#                first_name text,
#                last_name text,
#                address text,
#                city text,
#                state text,
 #               post_code integer)
 #           """)
def delete():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM addresses WHERE oid=" + delete_box.get())


    conn.commit()
    conn.close()

def submit():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("INSERT INTO addresses VALUES(:f_name, :l_name, :address, :city, :state, :p_code)",
    {
        'f_name': f_name.get(),
        'l_name': l_name.get(),
        'address': address.get(),
        'city': city.get(),
        'state': state.get(),
        'p_code': p_code.get()
    })

    conn.commit()
    conn.close()

    f_name.delete(0,END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    p_code.delete(0, END)

def query():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    cur.execute("SELECT *, oid FROM addresses")
    records = cur.fetchall()
    print(records)
    print_records = ''

    for record in records:
        print_records += str(record[0]) + " " + str(record[1]) + " " + "\t" + str(record[6]) + "\n"

    query_label =Label(root, text=print_records)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()


f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10,0))
l_name = Entry(root, width=30)
l_name.grid(row=1, column=1)
address = Entry(root, width=30)
address.grid(row=2, column=1)
city = Entry(root, width=30)
city.grid(row=3, column=1)
state = Entry(root, width=30)
state.grid(row=4, column=1)
p_code = Entry(root, width=30)
p_code.grid(row=5, column=1)

delete_box = Entry(root, width=10)
delete_box.grid(row=9, column=1)

f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, padx=20, pady=(10,0))
l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)
address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)
city_label = Label(root, text="City")
city_label.grid(row=3, column=0)
state_label = Label(root, text="County")
state_label.grid(row=4, column=0)
p_code_label = Label(root, text="Post Code")
p_code_label.grid(row=5, column=0)
delete_box_label = Label(root, text="Delete Number")
delete_box_label.grid(row=9, column=0)

submit_btn = Button(root, text="Submit Record", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

conn.commit()
conn.close()

root.mainloop()

