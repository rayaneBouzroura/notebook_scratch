import tkinter as tk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Minimalist Editor")
        
        # Create main text widget
        self.text_area = tk.Text(self.root, wrap='word', undo=True)
        self.text_area.pack(expand=True, fill='both')
        
        # Basic key bindings
        self.setup_bindings()
    
    def setup_bindings(self):
        # We'll expand this later for custom key handling
        self.text_area.bind('<KeyPress>',self.on_key_press)
        pass

    def on_key_press(self, event):
        #print data on pressed key
        print(f"key pressed : {event.char!r} (keycode : {event.keycode})")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()