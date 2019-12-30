from tkinter import *
import sqlite3

root = Tk()
root.title('Create Entry')
root.geometry("400x600")

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
def update():
    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()

    record_id = delete_box.get()
    cur.execute("""UPDATE addresses SET
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        post_code = :post_code
        
        WHERE oid = :oid""",
                {
                    'first': f_name_editor.get(),
                    'last': l_name_editor.get(),
                    'address': address_editor.get(),
                    'city': city_editor.get(),
                    'state': state_editor.get(),
                    'post_code': p_code_editor.get(),
                    'oid': record_id
                })

    conn.commit()
    conn.close()

def edit():
    editor = Tk()
    editor.title('Update a Record')
    editor.geometry("400x600")

    conn = sqlite3.connect('address_book.db')
    cur = conn.cursor()
    record_id = delete_box.get()

    cur.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = cur.fetchall()

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global p_code_editor

    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))
    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1)
    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1)
    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1)
    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1)
    p_code_editor = Entry(editor, width=30)
    p_code_editor.grid(row=5, column=1)

    f_name_label = Label(editor, text="First Name")
    f_name_label.grid(row=0, column=0, padx=20, pady=(10, 0))
    l_name_label = Label(editor, text="Last Name")
    l_name_label.grid(row=1, column=0)
    address_label = Label(editor, text="Address")
    address_label.grid(row=2, column=0)
    city_label = Label(editor, text="City")
    city_label.grid(row=3, column=0)
    state_label = Label(editor, text="County")
    state_label.grid(row=4, column=0)
    p_code_label = Label(editor, text="Post Code")
    p_code_label.grid(row=5, column=0)

    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        p_code_editor.insert(0, record[5])

    save_btn = Button(editor, text="Save Record", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

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
    query_label.grid(row=15, column=0, columnspan=2)

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

edit_btn = Button(root, text="Edit Record", command=edit)
edit_btn.grid(row=11, column=0, columnspan=2, padx=10, pady=10, ipadx=105)

conn.commit()
conn.close()

root.mainloop()

