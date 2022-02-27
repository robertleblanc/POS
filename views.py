import tkinter as tk
from tkinter import ttk
import db
import frames
from connector import Connector


class MainWindow(tk.Tk):
    def __init__(self, _database):
        super().__init__()
        # self.geometry('500x500')
        self.db = _database
        self.title('OHS - Point of Sale')

        connector = Connector()

        main_frame = frames.TreeFrame(self, connector, self.db)
        main_frame.pack()

        inputs_frame = frames.InputFrame(self, connector, self.db)
        inputs_frame.pack()

        connector.register(
            "update_inputs",
            inputs_frame.update
        )

        connector.register(
            "update_treeview",
            main_frame.update
        )

        connector.register(
            "refresh",
            main_frame.refresh_records
        )

    def loop(self):
        self.mainloop()
