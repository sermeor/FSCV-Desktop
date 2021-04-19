from libraries import *
class ACQUISITION_CONFIG:
    def __init__(self, parent_class):
        self.master = tk.Toplevel(parent_class.master,  bg='white')
        self.master.title('Acquisition Config.')
        self.master.transient(parent_class.master)
        self.master.grab_set()
        self.parent_class = parent_class
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.frequency_input = self.parent_class.gui_methods.get_input_object(self.main_frame, 'Acq. Freq.', 'white', [0,0,1,1,0,0], [0,1,1,1,0,0], self.parent_class.acquisition.frequency)
        self.cyclic_frequency_input = self.parent_class.gui_methods.get_input_object(self.main_frame, 'Cyc. Freq.', 'white', [1,0,1,1,0,0], [1,1,1,1,0,0], self.parent_class.acquisition.cycling_frequency)
        self.acquisition_time = self.parent_class.gui_methods.get_input_object(self.main_frame, 'Total Time', 'white', [2,0,1,1,0,0], [2,1,1,1,0,0], self.parent_class.acquisition.total_acquisition_time)


        self.apply_button = self.parent_class.gui_methods.get_button_object(self.main_frame, self.apply_changes_pushed, 2, 10, 'Apply', [3,0,2,1,0,0],'#3f51b5', 'white')
        self.close_button = self.parent_class.gui_methods.get_button_object(self.main_frame, self.close_button_pushed, 2, 10, 'Close', [3,1,2,1,0,0],'#3f51b5', 'white')

    def apply_changes_pushed(self):
            self.parent_class.acquisition.frequency = self.frequency_input.get()
            self.parent_class.acquisition.cycling_frequency = int(self.cyclic_frequency_input.get())
            self.parent_class.acquisition.total_acquisition_time = int(self.acquisition_time.get())

    def close_button_pushed(self):
            self.master.destroy()
