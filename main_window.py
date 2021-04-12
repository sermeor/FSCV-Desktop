#Imports for the application.
import tkinter as tk
import serial
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.figure import Figure
#import classes
from serial_config import SERIAL_CONFIG
from graph_config import GRAPH_CONFIG
from plot_settings import PLOT_SETTINGS
#Main window class.
class MAIN_WINDOW:
    def __init__(self):
        #Definition of app window.
        self.master = tk.Tk()
        self.master.title('FSCV Desktop App')
        self.width, self.height = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry('%dx%d+0+0' % (self.width,self.height))
        self.master.configure(bg='white')
        #
        #Define menu bar.
        self.menubar = tk.Menu(self.master)

        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.file_menu.add_command(label='Serial Config.', command=self.serial_config_button_pushed)
        self.file_menu.add_command(label='Graph Config.', command=self.graph_config_button_pushed)
        self.file_menu.add_command(label='Reset', command=self.reset_button_pushed)
        self.file_menu.add_command(label='Exit', command=self.exit_button_pushed)
        self.menubar.add_cascade(label="File", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Edit', menu=self.edit_menu)
        #Add menubar.
        self.master.config(menu = self.menubar)
        #Create resizable grid.
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.serial_frame = tk.Frame(self.main_frame, bg='white')
        self.serial_frame.grid(row=0, column=0, padx=5, pady=5)

        self.color_plot_frame = tk.Frame(self.main_frame, bg='white')
        self.color_plot_frame.grid(row=0, column=2, padx=5, pady=5)

        #Populating the serial frame.
        self.connect_button = self.get_button_object(self.serial_frame, self.connect_button_pushed, 2, 10, 'Connect', [4,0,1,2,0,0], '#3f51b5', 'white')

        #Initialisation of variables.
        self.serial_port = 'COM5'
        self.serial_bytes = 8
        self.serial_baud_rate = 115200
        #Graph color plots.
        self.plot_configuration = PLOT_SETTINGS()
        self.color_palette = self.plot_configuration.custom1
        

        ##TESTING ###################################################################################################################################
        self.get_color_plot(self.color_plot_frame, 5, 5, 100, 'Time (s)', 'Samples', 15, [0,1,1,1,10,10], self.plot_configuration.custom1)


    def get_color_plot(self, macro, size_x, size_y, dpi, x_label, y_label, fontsize, position, color_palette):
        fig = Figure(figsize=(size_x, size_y), dpi=dpi)
        axes = fig.add_subplot(111)
        axes.set_ylabel(y_label, fontsize=fontsize)
        axes.set_xlabel(x_label, fontsize=fontsize)
        axes.tick_params(axis='both', labelsize=15)
        matrix = axes.imshow(np.random.rand(300,300), cmap=color_palette)
        divider = make_axes_locatable(axes)
        cax2 = divider.append_axes("right", size="5%", pad=0.05)
        fig.colorbar(matrix, cax=cax2)
        fig.tight_layout()
        canvas = FigureCanvasTkAgg(fig, master=macro)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=position[0], column=position[1], rowspan=position[2], columnspan=position[3], padx=position[4], pady=position[5])
        return fig, axes, matrix, canvas, plot_widget

    def get_3D_plot(self):

        return False

        ##TESTING ###################################################################################################################################
    def get_input_object(self, macro, label_name, color, label_position, input_position, default_value):
        tk.Label(macro, text=label_name, bg=color).grid(row=label_position[0], column=label_position[1],
        rowspan=label_position[2], columnspan=label_position[3], padx=label_position[4], pady=label_position[5])
        input = tk.Entry(macro)
        input.insert(0, default_value)
        input.grid(row=input_position[0], column=input_position[1], rowspan=input_position[2],
        columnspan=input_position[3], padx=input_position[4], pady=input_position[5])
        return input

    def get_button_object(self, macro, callback_fcn, height, width, text, position, color, text_color):
        button = tk.Button(master = macro, command = callback_fcn, height = height, width = width, text = text, bg=color, fg=text_color)
        button.grid(row=position[0], column=position[1], rowspan=position[2], columnspan=position[3], padx=position[4], pady=position[5])
        return button


    def connect_button_pushed(self):
        if self.connect_button['text'] == 'Connected':
            self.disconnect_from_serial_port()
        else:
            self.connect_to_serial_port()

    def connect_to_serial_port(self):
        try:
            self.serial_connection = serial.Serial(self.serial_port, self.serial_baud_rate, self.serial_bytes)
            self.connect_button.configure(bg="#94FF98", text='Connected')
        except:
            tk.messagebox.showerror(title='Error', message='Connection to '+self.serial_port+' unsuccesful')

    def disconnect_from_serial_port(self):
        self.serial_connection.close()
        self.connect_button.configure(bg='#3f51b5', text = 'Connect')

    def serial_config_button_pushed(self):
        self.serial_config = SERIAL_CONFIG(self)
        #self.master.wait_window(self.serial_config.master)

    def graph_config_button_pushed(self):
        self.graph_config = GRAPH_CONFIG(self)

    def reset_button_pushed(self):
        self.master.destroy()
        start_application()


    def exit_button_pushed(self):
        self.master.destroy()

#Initialisation of the application
def start_application():
    global main_window
    main_window = MAIN_WINDOW()
    main_window.master.mainloop()

start_application()
