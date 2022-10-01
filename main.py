from gui import mainApplication as mainApp
from util import dbconnection as db
from util import accounts
import tkinter as tk
import time

if __name__ == "__main__":
    # root = tk.Tk()
    # mainApp.MainApplication(root).pack(side="top", fill="both", expand=True)
    # root.mainloop()
    currAccount = accounts.Accounts('test', 'test')
    currAccount.login()

