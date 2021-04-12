import tkinter as tk
class GRAPH_CONFIG:
    def __init__(self, parent_class):
        self.master = tk.Toplevel(parent_class.master,  bg='white')
        self.master.title('Graph Config.')
        self.master.transient(parent_class.master)
        self.master.grab_set()
        self.parent_class = parent_class
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.color_palette = 'Custom'
        self.color_palette_list = ('Custom', 'IBM', 'Wang')
        tk.Label(self.main_frame, text='Color palette', bg='white').grid(row=0, column=0, rowspan=1, columnspan=1, padx=0, pady=0)
        self.color_palette_selection = tk.OptionMenu(self.main_frame, self.color_palette, *self.color_palette_list)
        self.color_palette_selection.grid(row=0, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

        self.apply_button = self.parent_class.get_button_object(self.main_frame, self.apply_changes_pushed, 2, 10, 'Apply', [3,0,2,1,0,0],'#3f51b5', 'white')
        self.close_button = self.parent_class.get_button_object(self.main_frame, self.close_button_pushed, 2, 10, 'Close', [3,1,2,1,0,0],'#3f51b5', 'white')

    def apply_changes_pushed(self):
        self.master.destroy()

    def close_button_pushed(self):
        self.master.destroy()
