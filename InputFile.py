# GUI for inputting a file with Tkinter

from tkinter import messagebox, filedialog
from tkinter import *

root = Tk()
root.withdraw()

def importFile():
    
    messagebox.showinfo('Please Select A File', 'Please Select A File')
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                      filetypes = (("CSV files","*.csv"),("All Files","*.*")))
    
    if not filename:
        print('No file')
        root.destroy()
    else:
        return filename

importFile()
