from libraries import *
class SERIAL_CONFIG:
    def __init__(self, parent_class):
        self.master = tk.Toplevel(parent_class.master,  bg='white')
        self.master.title('Serial Config.')
        self.master.transient(parent_class.master)
        self.master.grab_set()
        self.parent_class = parent_class
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.serial_port_input = self.parent_class.get_input_object(self.main_frame, 'Serial port', 'white', [0,0,1,1,0,0], [0,1,1,1,0,0], self.parent_class.serial.port)
        self.bytes_input = self.parent_class.get_input_object(self.main_frame, 'Bytes', 'white', [1,0,1,1,0,0], [1,1,1,1,0,0], str(self.parent_class.serial.bytes))
        self.baud_rate_input = self.parent_class.get_input_object(self.main_frame, 'Baud rate', 'white', [2,0,1,1,0,0], [2,1,1,1,0,0], str(self.parent_class.serial.baud_rate))

        self.apply_button = self.parent_class.get_button_object(self.main_frame, self.apply_changes_pushed, 2, 10, 'Apply', [3,0,2,1,0,0],'#3f51b5', 'white')
        self.close_button = self.parent_class.get_button_object(self.main_frame, self.close_button_pushed, 2, 10, 'Close', [3,1,2,1,0,0],'#3f51b5', 'white')

    def apply_changes_pushed(self):
        self.parent_class.serial.port = self.serial_port_input.get()
        self.parent_class.serial.bytes = int(self.bytes_input.get())
        self.parent_class.serial.baud_rate = int(self.baud_rate_input.get())

    def close_button_pushed(self):
        self.master.destroy()
