import tkinter as tk
from tkinter import ttk
from connector import Connector
import db


class TreeFrame(ttk.Labelframe):
    def __init__(self, container, _connector, _db):
        super().__init__(container)

        self.db = _db

        self.connector = _connector
        options = {
            'text': "Database",
            'padding': 20
        }

        self.config(options)
        self.columns = ('id', 'Last', 'First', 'rfid', 'Balance')

        self.my_tree = ttk.Treeview(
            self,
            columns=self.columns,
            show='headings',
            selectmode='browse'
        )

        self.my_tree.column('id', anchor=tk.W, width=40)
        self.my_tree.column('Last', anchor=tk.W, width=120)
        self.my_tree.column('First', anchor=tk.W, width=120)
        self.my_tree.column('rfid', anchor=tk.W, width=80)
        self.my_tree.column('Balance', anchor=tk.W, width=80)

        self.my_tree.heading('id', text='ID', anchor=tk.W)
        self.my_tree.heading('Last', text='Lastname', anchor=tk.W)
        self.my_tree.heading('First', text='Firstname', anchor=tk.W)
        self.my_tree.heading('rfid', text='RFID', anchor=tk.W)
        self.my_tree.heading('Balance', text='Balance', anchor=tk.W)

        self.my_tree.bind('<<TreeviewSelect>>', self.select_record)

        self.my_tree.pack(pady=20)

    def insert_records(self, _records):
        for row in _records:
            self.my_tree.insert('', tk.END, values=row)

    def select_record(self, e):
        selected = self.my_tree.focus()
        values = self.my_tree.item(selected, 'values')
        self.connector.update("update_inputs", values)

    def update(self, _values):
        selected = self.my_tree.focus()
        self.my_tree.item(
            selected,
            text="",
            values=(
                _values['id'],
                _values['last'],
                _values['first'],
                _values['rfid'],
                _values['balance'],
            )
        )


class InputFrame(ttk.Labelframe):
    def __init__(self, container, _connector, _db):
        super().__init__(container)
        # self.db
        self.options = {
            'text': "Edit Record",
            'padding': 20
        }
        self.db = _db
        self.connector = _connector

        self.id_label = tk.Label(self, text="ID:")
        self.id_label.grid(row=0, column=0, padx=10, pady=10)
        self.id_entry = tk.Entry(self)
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        # ID should not be changed
        self.id_entry.config(state=tk.DISABLED)

        self.ln_label = tk.Label(self, text="Lastname:")
        self.ln_label.grid(row=0, column=2, padx=10, pady=10)
        self.ln_entry = tk.Entry(self)
        self.ln_entry.grid(row=0, column=3, padx=10, pady=10)

        self.fn_label = tk.Label(self, text="Firstname:")
        self.fn_label.grid(row=0, column=4, padx=10, pady=10)
        self.fn_entry = tk.Entry(self)
        self.fn_entry.grid(row=0, column=5, padx=10, pady=10)

        self.rfid_label = tk.Label(self, text="RFID:")
        self.rfid_label.grid(row=1, column=0, padx=10, pady=10)
        self.rfid_entry = tk.Entry(self)
        self.rfid_entry.grid(row=1, column=1, padx=10, pady=10)

        self.balance_label = tk.Label(self, text="Balance:")
        self.balance_label.grid(row=1, column=2, padx=10, pady=10)
        self.balance_entry = tk.Entry(self)
        self.balance_entry.grid(row=1, column=3, padx=10, pady=10)

        self.submit = ttk.Button(self, text="Submit", command=self.submit)
        self.submit.grid(row=2, column=5, padx=10, pady=10)

    def update(self, _values):
        self.id_entry.config(state='normal')
        self.id_entry.delete(0, tk.END)
        self.ln_entry.delete(0, tk.END)
        self.fn_entry.delete(0, tk.END)
        self.rfid_entry.delete(0, tk.END)
        self.balance_entry.delete(0, tk.END)

        self.id_entry.insert(0, _values[0])
        self.id_entry.config(state='disabled')
        self.ln_entry.insert(0, _values[1])
        self.fn_entry.insert(0, _values[2])
        self.rfid_entry.insert(0, _values[3])
        self.balance_entry.insert(0, _values[4])

    def submit(self):
        id = self.id_entry.get()
        values = {
            'id': self.id_entry.get(),
            'last': self.ln_entry.get(),
            'first': self.fn_entry.get(),
            'rfid': self.rfid_entry.get(),
            'balance': self.balance_entry.get()
        }

        self.db.update_by_id(id, values)
        self.connector.update("update_treeview", values)