from tkinter import Tk, Frame, Button, Text
from tkinter.ttk import Frame, Button
from tkinter.filedialog import askopenfile
from tkinter.messagebox import showerror

class Application(Frame):

    def __init__(self, root, title, geometry = None):
        self.root = root
        self.root.title(title)
        
        self.file_handle = ""

        master_frame = Frame(root)
        master_frame.pack(expand="yes", fill="both")
        
        button_frame = Frame(master_frame)
        self.open_button = Button(button_frame, text="Choose File", command=self.load_file)
        self.open_button.pack(expand="yes", fill="both")
        self.apply_button = Button(button_frame, text="Apply", command=self.apply_consistent, state="disabled")
        self.apply_button.pack(expand="yes", fill="both")
        self.save_button = Button(button_frame, text="Save File", command=self.save_file, state="disabled")
        self.save_button.pack(expand="yes", fill="both")

        text_frame = Frame(master_frame)
        self.text_box = Text(text_frame, height=10, width=50, state="disabled")
        self.text_box.pack(side="top", expand="yes", fill="both")

        for i in range(3):
            master_frame.rowconfigure(i, weight=1)
        for i in range(2):
            master_frame.columnconfigure(i, weight=1)

        button_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        text_frame.grid(row=0, column=1, rowspan=3, columnspan=3, sticky="nsew")
        
        self.root.minsize(500, 200)


    def load_file(self):
        fname = askopenfile(mode='r', filetypes=([("Cascading Style Sheet Document", "*.css")]))
        self.file_handle = fname

        if fname:
            self.apply_button['state'] = 'enabled'
            self.save_button['state'] = 'enabled'
            self.change_text(fname.read())
            self.parse_file(fname)


    def parse_file(self, file_handle):
        return


    def apply_consistent(self):
        return
    

    def save_file(self):
        return


    def change_text(self, text):
        self.text_box['state'] = 'normal'
        self.text_box.insert(END, text)
        self.text_box['state'] = 'disabled'
        

def main():
    root = Tk()
    Application(root, "Consistent CSS")
    root.mainloop()


if __name__ == '__main__':
    main()
