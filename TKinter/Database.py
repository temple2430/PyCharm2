from tkinter import *
import sqlite3

root = Tk()

conn = sqlite3.connect('address_book.db')

cur = conn.cursor()

cur.execute("""CREATE TABLE addresses(
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                post_code integer)
            """)

conn.commit()

conn.close()



root.mainloop()

