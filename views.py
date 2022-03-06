import tkinter
import frames


class MainWindow(tkinter.Tk):
    def __init__(self, _database):
        super().__init__()
        # self.geometry('500x500')
        self.db = _database
        self.title('OHS - Point of Sale')

        self.main_frame = frames.TreeFrame(self, self.db)
        self.main_frame.pack()

        self.inputs_frame = frames.InputFrame(self, self.db)
        self.inputs_frame.pack()

    def loop(self):
        self.mainloop()
