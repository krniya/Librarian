from gui import mainApplication as mainApp
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    mainApp.MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()