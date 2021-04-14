from libraries import *
class SERIAL_SETTINGS:
    def __init__(self, parent_class):
        self.port = 'COM5'
        self.bytes = 8
        self.baud_rate = 115200
        self.parent_class = parent_class

    def connect_to_serial_port(self):
        try:
            self.serial_connection = serial.Serial(self.port, self.baud_rate, self.bytes)
            self.parent_class.connect_button.configure(bg="#94FF98", text='Connected')
        except:
            tk.messagebox.showerror(title='Error', message='Connection to '+self.port+' unsuccesful')

    def disconnect_from_serial_port(self):
        self.serial_connection.close()
        self.parent_class.connect_button.configure(bg='#3f51b5', text = 'Connect')
