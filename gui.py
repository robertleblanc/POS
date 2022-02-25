# import tkinter as tk
import tkinter as tk
from tkinter import ttk
import db

database = db.Database()

# root window
wnd = tk.Tk()
wnd.title('OHS - Point of Sale')
wnd.geometry('500x500')

columns = ('id', 'Last', 'First', 'rfid', 'Balance')

my_tree = ttk.Treeview(wnd, columns=columns, show='headings')


def item_selected(event):
    selected = my_tree.item(my_tree.selection())
    print(selected)


my_tree.column('id', anchor=tk.W, width=40)
my_tree.column('Last', anchor=tk.W, width=120)
my_tree.column('First', anchor=tk.W, width=120)
my_tree.column('rfid', anchor=tk.W, width=80)
my_tree.column('Balance', anchor=tk.W, width=80)

my_tree.heading('id', text='ID', anchor=tk.W)
my_tree.heading('Last', text='Lastname', anchor=tk.W)
my_tree.heading('First', text='Firstname', anchor=tk.W)
my_tree.heading('rfid', text='RFID', anchor=tk.W)
my_tree.heading('Balance', text='Balance', anchor=tk.W)

my_tree.bind('<<TreeviewSelect>>', item_selected)

rows = database.read_all()

for row in rows:
    my_tree.insert('', tk.END, values=row)

my_tree.pack(pady=20)

wnd.mainloop()
