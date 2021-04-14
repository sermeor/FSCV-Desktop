from libraries import *
class GRAPH_CONFIG:
    def __init__(self, parent_class):
        self.master = tk.Toplevel(parent_class.master,  bg='white')
        self.master.title('Graph Config.')
        self.master.transient(parent_class.master)
        self.master.grab_set()
        self.parent_class = parent_class
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.color_palette_name = tk.StringVar()
        self.color_palette_name.set(self.parent_class.fscv_data.color_palette_name)
        self.color_palette_namelist = ('Custom', 'IBM', 'Wang', 'Grays')

        tk.Label(self.main_frame, text='Color palette', bg='white').grid(row=0, column=0, rowspan=1, columnspan=1, padx=0, pady=0)
        self.color_palette_selection = tk.OptionMenu(self.main_frame, self.color_palette_name, *self.color_palette_namelist)
        self.color_palette_selection.grid(row=0, column=1, rowspan=1, columnspan=1, padx=0, pady=0)

        self.upper_bound_input = self.parent_class.get_input_object(self.main_frame, 'Upper bound', 'white', [1,0,1,1,0,0], [1,1,1,1,0,0], self.parent_class.fscv_data.color_upper_bound)
        self.lower_bound_input = self.parent_class.get_input_object(self.main_frame, 'Lower bound', 'white', [2,0,1,1,0,0], [2,1,1,1,0,0], self.parent_class.fscv_data.color_lower_bound)

        self.apply_button = self.parent_class.get_button_object(self.main_frame, self.apply_changes_pushed, 2, 10, 'Apply', [3,0,2,1,0,0],'#3f51b5', 'white')
        self.close_button = self.parent_class.get_button_object(self.main_frame, self.close_button_pushed, 2, 10, 'Close', [3,1,2,1,0,0],'#3f51b5', 'white')

    def apply_changes_pushed(self):
        #change color palette in parent class.
        self.parent_class.fscv_data.color_palette_name = self.color_palette_name.get()
        if self.parent_class.fscv_data.color_palette_name == self.color_palette_namelist[0]:
            self.parent_class.fscv_data.color_palette = self.parent_class.plot_configuration.custom
        elif self.parent_class.fscv_data.color_palette_name == self.color_palette_namelist[1]:
            self.parent_class.fscv_data.color_palette = self.parent_class.plot_configuration.ibm
        elif self.parent_class.fscv_data.color_palette_name == self.color_palette_namelist[2]:
            self.parent_class.fscv_data.color_palette = self.parent_class.plot_configuration.wang
        elif self.parent_class.fscv_data.color_palette_name == self.color_palette_namelist[3]:
            self.parent_class.fscv_data.color_palette = self.parent_class.plot_configuration.grays
        #change limits of color palette.
        self.parent_class.fscv_data.color_upper_bound = self.upper_bound_input.get()
        self.parent_class.fscv_data.color_lower_bound = self.lower_bound_input.get()
        #Regraph the color plot.
        self.parent_class.fscv_data.change_color_palette()

    def close_button_pushed(self):
        self.master.destroy()
