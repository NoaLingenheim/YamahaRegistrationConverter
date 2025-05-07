import tkinter as tk
from tkinter import filedialog
import os
import sys


ConvertingFrom = "GENOS 2"
ConvertingTo = "GENOS 1"

FileToConvert = ""
newfilepath = ""

def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.abspath("."), relative_path)


def SelectFile():
    global FileToConvert
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            with open(file_path, 'rb') as f:
                binary_values = list(f.read())
            FileToConvert = file_path
        except Exception as e:
            print(f"Error reading file: {e}")
            tk.messagebox.showerror("Error", f"Could not read the file.")

def SaveFile():
    global newfilepath
    newfilepath = filedialog.asksaveasfilename(defaultextension=".rgt", filetypes=[("GENOS 1 files", "*.rgt")])
    if newfilepath:
        try:
            with open(newfilepath, 'wb') as f:
                f.write(b'')
        except Exception as e:
            print(f"Error saving file: {e}")
            tk.messagebox.showerror("Error", f"Could not save the file.")


def ConvertFile():
    global FileToConvert
    global newfilepath

    if FileToConvert:
        if not newfilepath:
            tk.messagebox.showerror("Error", "Please select a save location.")
            return
        if not FileToConvert:
            tk.messagebox.showerror("Error", "Please select a file to convert.")
            return
        if not os.path.exists(FileToConvert):
            tk.messagebox.showerror("Error", "File to convert does not exist.")
            return
        

        with open(FileToConvert, 'rb') as f:
            binary_values1 = list(f.read())
        with open(get_resource_path("genos1.data"), 'rb') as f:
            binary_values2 = list(f.read())

        datatosave = []
        for i in range(len(binary_values1)):
            if i <= 48:
                datatosave.append(binary_values2[i])
            else:
                datatosave.append(binary_values1[i])
        
        os.remove(newfilepath)

        toconvertfilenamesplited = os.path.basename(FileToConvert).split(".")
        newfilenamesplited = os.path.basename(newfilepath).split(".")
        newfilename = newfilenamesplited[0] + "." + toconvertfilenamesplited[len(toconvertfilenamesplited)-2] + ".rgt"
        newfilepath = os.path.join(os.path.dirname(newfilepath), newfilename)

       
        
        with open(newfilepath, 'wb') as f:
            f.write(bytearray(datatosave))

        tk.messagebox.showinfo("Success", f"File converted successfully and saved as {newfilename}.")

        

root = tk.Tk()
root.title("Yamaha Registration Converter")
root.geometry("800x400")
root.configure(bg="black")
root.resizable(False, False)
root.iconbitmap(get_resource_path("icon.ico"))  # Load the icon from the resource path


label = tk.Label(root, text=f"Converting from {ConvertingFrom} to {ConvertingTo}.", bg="black", fg="white", font=("Arial", 16))
label.pack(pady=20)



select_button = tk.Button(root, text="Select File", command=SelectFile, bg="black", fg="white", font=("Arial", 14))
select_button.pack(pady=20)

save_button = tk.Button(root, text="Save As", command=SaveFile, bg="black", fg="white", font=("Arial", 14))
save_button.pack(pady=20)


convert_button = tk.Button(root, text="Convert", command=ConvertFile, bg="black", fg="white", font=("Arial", 14))
convert_button.pack(pady=20)

label2 = tk.Label(root, text="Made by Noa LINGENHEIM (Zurdioz)", bg="black", fg="white", font=("Arial", 10))
label2.pack(pady=20)



    
root.mainloop()




