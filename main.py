from gui import mainApplication as mainApp
from util import dbconnection as db
import tkinter as tk
import time

if __name__ == "__main__":
    # root = tk.Tk()
    # mainApp.MainApplication(root).pack(side="top", fill="both", expand=True)
    # root.mainloop()
    dbConect = db.DatabaseConnect()
    time.sleep(5)
    dbConect.disconnect()

