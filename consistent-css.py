from tkinter import Tk, Frame, Button, Text
from tkinter.ttk import Frame, Button
from tkinter.filedialog import askopenfile

class Application():
    def __init__(self, root, title):
        self.root = root
        self.root.title(title)

        # Variable that stores file handle (may be unnecessary)
        self.file_handle = ""

        master_frame = Frame(root)
        master_frame.pack(expand="yes", fill="both")

        # Create left button frame and buttons
        button_frame = Frame(master_frame)
        self.open_button = Button(button_frame, text="Choose File", command=self.load_file)
        self.open_button.pack(expand="yes", fill="both")
        self.apply_button = Button(button_frame, text="Apply", command=self.apply_consistent, state="disabled")
        self.apply_button.pack(expand="yes", fill="both")
        self.save_button = Button(button_frame, text="Save File", command=self.save_file, state="disabled")
        self.save_button.pack(expand="yes", fill="both")

        # Create text frame and initialize text widget
        text_frame = Frame(master_frame)
        self.text_box = Text(text_frame, height=10, width=50, state="disabled")
        self.text_box.pack(side="top", expand="yes", fill="both")

        # Configure weights for grid elements
        master_frame.columnconfigure(0, weight=1)
        master_frame.columnconfigure(1, weight=5)
        for i in range(3):
            master_frame.rowconfigure(i, weight=1)

        # Position button and text frames
        button_frame.grid(row=0, column=0, rowspan=3, sticky="nsew")
        text_frame.grid(row=0, column=1, rowspan=3, sticky="nsew")
        
        self.root.minsize(500, 200)


    # Function which prompts user to select css file to open
    def load_file(self):
        fname = askopenfile(mode='r', filetypes=([("Cascading Style Sheet Document", "*.css")]))
        self.file_handle = fname

        if fname:
            self.apply_button["state"] = "enabled"      # Enables other button after successful
            self.save_button["state"] = "enabled"       # file load
            self.change_text(fname.read())
            self.parse_file(fname)


    # Function to parse readlines to a more managable form
    def parse_file(self, file_handle):
        return


    # Function to potentially apply sorting scheme to file contents
    def apply_consistent(self):
        return
    

    # To be called when save button is pressed and will allow user to save as they wish
    def save_file(self):
        return


    # Function used to edit text field
    def change_text(self, text):
        self.text_box["state"] = "normal"       # Enables text widget for editing
        self.text_box.delete(1.0, "end")        # Clears current text
        self.text_box.insert("end", text)       # Enters file contents to text widget
        self.text_box["state"] = "disabled"     # Re-disables text widget
        

def main():
    root = Tk()
    Application(root, "Consistent CSS")
    root.mainloop()


if __name__ == '__main__':
    main()
