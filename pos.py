import views
import db


class App:
    def __init__(self):

        database = db.Database()
        w = views.MainWindow(database)
        w.loop()


app = App()
