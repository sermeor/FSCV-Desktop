from libraries import *
#import classes
from gui_methods import GUI_METHODS # Methods to build the GUIs.
from fscv_data import FSCV_DATA #Classes to store the data and methods.
from serial_config import SERIAL_CONFIG #Serial configuration popup window.
from graph_config import GRAPH_CONFIG #Graph configuration popup window.
from acquisition_config import ACQUISITION_CONFIG # Acquisition configuration popup window.
from waveform_config import WAVEFORM_CONFIG #Waveform configuration popup window.
from plot_settings import PLOT_SETTINGS #Plot settings.
from serial_settings import SERIAL_SETTINGS #serial connection parameters.
from acquisition_settings import ACQUISITION_SETTINGS # Acquisition parameters.
from waveform_settings import WAVEFORM_SETTINGS # Waveform parameters.
from oscilloscope_window import OSCILLOSCOPE_WINDOW # Oscilloscope class for the window.

#Main window class.
class MAIN_WINDOW:
    def __init__(self):
        #Definition of app window.
        self.master = tk.Tk()
        self.master.title('FSCV Desktop App')
        self.width, self.height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry('%dx%d+0+0' % (self.width,self.height))
        self.master.configure(bg='white')
        #GUI methods.
        self.gui_methods = GUI_METHODS()
        #Define menu bar.
        self.menubar = tk.Menu(self.master)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='Serial Config.', command=self.serial_config_button_pushed)
        self.file_menu.add_command(label='Graph Config.', command=self.graph_config_button_pushed)
        self.file_menu.add_command(label='Acquisition Config.', command=self.acquisition_config_button_pushed)
        self.file_menu.add_command(label='Waveform Config.', command=self.waveform_config_button_pushed)
        self.file_menu.add_command(label='Reset', command=self.reset_button_pushed)
        self.file_menu.add_command(label='Exit', command=self.exit_button_pushed)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.tools_menu = tk.Menu(self.menubar, tearoff=0)
        self.tools_menu.add_command(label='Analysis application', command=self.analysis_application_button_pushed)
        self.tools_menu.add_command(label='Oscilloscope', command=self.oscilloscope_button_pushed)
        self.menubar.add_cascade(label='Tools', menu=self.tools_menu)

        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=self.edit_menu)

        self.help_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Help', menu=self.help_menu)
        #Add menubar.
        self.master.config(menu = self.menubar)
        #Create resizable grid.
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.serial_frame = tk.Frame(self.main_frame, bg='white')
        self.serial_frame.grid(row=0, column=0, padx=5, pady=5)

        self.color_plot_frame = tk.Frame(self.main_frame, bg='white')
        self.color_plot_frame.grid(row=0, column=2, padx=5, pady=5)

        self.color_plot_toolbar_frame = tk.Frame(self.main_frame, bg='white')
        self.color_plot_toolbar_frame.grid(row=1, column=2, padx=5, pady=5)

        self.voltage_XY_frame = tk.Frame(self.main_frame, bg='white')
        self.voltage_XY_frame.grid(row=0, column=3, padx=5, pady=5)

        #Populating the serial frame.
        self.connect_button = self.gui_methods.get_button_object(self.serial_frame, self.connect_button_pushed, 2, 10, 'Connect', [4,0,1,2,0,0], '#3f51b5', 'white')
        self.apply_waveform_button = self.gui_methods.get_button_object(self.serial_frame, self.apply_waveform_button_pushed, 2, 15, 'Apply waveform', [5,0,1,2,0,0], '#3f51b5', 'white')
        self.acquire_data_button = self.gui_methods.get_button_object(self.serial_frame, self.acquire_data_button_pushed, 2, 10, 'Acquire data', [6,0,1,2,0,0], '#3f51b5', 'white')

        #Initialisation of variables.
        self.serial = SERIAL_SETTINGS(self)

        self.plot_configuration = PLOT_SETTINGS()
        self.fscv_data = FSCV_DATA(self, 'nA', 's', 's', 'Current', 'Time', 'Time', -10, 10, 'Color plot', np.random.rand(3000,2000))
        self.fscv_data.init_color_plot(self.color_plot_frame, 5, 5, 100, 8, [0,1,1,1,10,10])
        self.acquisition = ACQUISITION_SETTINGS(self)

        #Radio buttons FSCV-FSCAV
        self.type_of_acquisition = tk.StringVar()
        self.fscv_button = tk.Radiobutton(self.serial_frame, text="FSCV", indicatoron=False, value='FSCV', variable=self.type_of_acquisition, width=8, selectcolor='#3f51b5', fg='white', command=self.type_of_acquisition_changed)
        self.fscv_button.select()
        self.fscv_button.grid(row=0, column=2)
        self.fscav_button = tk.Radiobutton(self.serial_frame, text="FSCAV", indicatoron=False, value='FSCAV', variable=self.type_of_acquisition, width=8, selectcolor='#3f51b5', command=self.type_of_acquisition_changed)
        self.fscav_button.grid(row=0, column=3)

        #Waveform settings
        self.waveform_settings = WAVEFORM_SETTINGS(self)





    def connect_button_pushed(self):
        if self.connect_button['text'] == 'Connected':
            self.serial.disconnect_from_serial_port()
        else:
            self.serial.connect_to_serial_port()

    def serial_config_button_pushed(self):
        self.serial_config = SERIAL_CONFIG(self)

    def graph_config_button_pushed(self):
        self.graph_config = GRAPH_CONFIG(self)

    def acquisition_config_button_pushed(self):
        self.acquisition_config = ACQUISITION_CONFIG(self)

    def waveform_config_button_pushed(self):
        self.waveform_config = WAVEFORM_CONFIG(self)

    def reset_button_pushed(self):
        self.master.destroy()
        start_application()


    def exit_button_pushed(self):
        self.master.destroy()

    def analysis_application_button_pushed(self):

        return False

    def apply_waveform_button_pushed(self):
        # if self.connect_button['text'] == 'Connected':
        #     self.serial.disconnect_from_serial_port()
        # else:
        #     self.serial.connect_to_serial_port()

        self.parent_class.apply_waveform_button.configure(bg="#94FF98", text='Applying waveform')


    def acquire_data_button_pushed(self):

        return False

    def acquisition_config_button_pushed(self):
        self.acquisition_window = ACQUISITION_CONFIG(self)

    def oscilloscope_button_pushed(self):
        self.oscilloscope_window = OSCILLOSCOPE_WINDOW(self)

    def type_of_acquisition_changed(self):
        if self.type_of_acquisition.get() == 'FSCV':
            self.fscv_button.configure(fg='white')
            self.fscav_button.configure(fg='black')
        else:
            self.fscv_button.configure(fg='black')
            self.fscav_button.configure(fg='white')
        #CONTINUE WITH ACTIONS TO CHANGE TYPE OF ACQUISITION

#Initialisation of the application
def start_application():
    global main_window
    main_window = MAIN_WINDOW()
    main_window.master.mainloop()

start_application()
