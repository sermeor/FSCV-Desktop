from libraries import *
class WAVEFORM_CONFIG:
    def __init__(self, parent_class):
        self.master = tk.Toplevel(parent_class.master,  bg='white')
        self.master.title('Waveform Config.')
        self.master.resizable(False, False)
        self.master.transient(parent_class.master)
        self.master.grab_set()
        self.parent_class = parent_class
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        #Tabs.
        self.tab_frame = ttk.Notebook(self.main_frame)
        self.edit_waveform_frame = tk.Frame(self.tab_frame, bg='white')
        self.saved_waveform_frame = tk.Frame(self.tab_frame, bg='white')
        self.point_based_waveform_frame = tk.Frame(self.tab_frame, bg='white')
        self.import_waveform_frame = tk.Frame(self.tab_frame, bg='white')
        self.tab_frame.add(self.saved_waveform_frame, text='Saved waveform')
        self.tab_frame.add(self.edit_waveform_frame, text='Simple waveform')
        self.tab_frame.add(self.point_based_waveform_frame, text='Coordinates waveform')
        self.tab_frame.add(self.import_waveform_frame, text='Import waveform')
        self.tab_frame.grid(row=0, column=0)
        #Buttons
        self.options_frame = tk.Frame(self.main_frame, bg='white')
        self.options_frame.grid(row=1, column = 0)

        self.apply_frame = tk.Frame(self.main_frame, bg='white')
        self.apply_frame.grid(row=1, column = 1)
        self.refresh_graph_button = self.parent_class.gui_methods.get_button_object(self.options_frame, self.refresh_waveform, 2, 10, 'Refresh', [0,0,1,1,0,0], '#3f51b5', 'white')
        self.export_waveform_button = self.parent_class.gui_methods.get_button_object(self.options_frame, self.export_waveform, 2, 10, 'Export', [0,1,1,1,0,0], '#3f51b5', 'white')
        #Variables.
        self.voltage_array = []
        self.time_array = []



        #Edit waveform panel
        self.scan_rate_input = self.parent_class.gui_methods.get_input_object(self.edit_waveform_frame, 'Scan rate (V/s)', 'white', [0,0,1,1,0,0], [0,1,1,1,0,0], self.parent_class.waveform_settings.scan_rate)
        self.low_potential_input = self.parent_class.gui_methods.get_input_object(self.edit_waveform_frame, 'Low potential (V)', 'white', [1,0,1,1,0,0], [1,1,1,1,0,0], self.parent_class.waveform_settings.low_potential)
        self.high_potential_input = self.parent_class.gui_methods.get_input_object(self.edit_waveform_frame, 'High potential (V)', 'white', [2,0,1,1,0,0], [2,1,1,1,0,0], self.parent_class.waveform_settings.high_potential)
        self.phase_shift_input = self.parent_class.gui_methods.get_input_object(self.edit_waveform_frame, 'Phase shift (%)', 'white', [3,0,1,1,0,0], [3,1,1,1,0,0], self.parent_class.waveform_settings.phase_shift)


        #Coordinates waveform.
        self.time_input = self.parent_class.gui_methods.get_input_object(self.point_based_waveform_frame, 'Time point (s)', 'white', [0,0,1,1,0,0], [0,1,1,1,0,0], 0)
        self.voltage_input = self.parent_class.gui_methods.get_input_object(self.point_based_waveform_frame, 'Voltage point (V)', 'white', [1,0,1,1,0,0], [1,1,1,1,0,0], 0)
        self.add_coordenates_button = self.parent_class.gui_methods.get_button_object(self.point_based_waveform_frame, self.add_point_to_table, 2, 5, 'Add', [0,2,2,1,0,0], '#3f51b5', 'white')
        self.remove_coordenates_button = self.parent_class.gui_methods.get_button_object(self.point_based_waveform_frame, self.remove_point_of_table, 2, 5, 'Del.', [0,3,2,1,0,0], '#3f51b5', 'white')
        self.list_of_coordinates = ttk.Treeview(self.point_based_waveform_frame, columns=('t', 'V'), height=3)
        self.list_of_coordinates.column("#0", width=0)
        self.list_of_coordinates.column("t", width=100)
        self.list_of_coordinates.column("V", width=100)
        self.list_of_coordinates.heading('t', text='Time (s)')
        self.list_of_coordinates.heading('V', text='Voltage (V)')
        self.list_of_coordinates.grid(row=2, column=0, columnspan=2)
        self.coordinates_array = []
        self.point_counter = 0

        #Saved waveform panel
        self.saved_waveform_variable = tk.StringVar()
        self.dopamine_button = tk.Radiobutton(self.saved_waveform_frame, text="DA", indicatoron=False, value='DA', variable=self.saved_waveform_variable, width=8, command=self.saved_waveform_changed)
        self.dopamine_button.select()
        self.dopamine_button.grid(row=0, column=0)
        self.serotonin_button = tk.Radiobutton(self.saved_waveform_frame, text="5-HT", indicatoron=False, value='5-HT', variable=self.saved_waveform_variable, width=8, command=self.saved_waveform_changed)
        self.serotonin_button.grid(row=1, column=0)
        self.histamine_serotonin_button = tk.Radiobutton(self.saved_waveform_frame, text="HA/5-HT", indicatoron=False, value='HA/5-HT', variable=self.saved_waveform_variable, width=8, command=self.saved_waveform_changed)
        self.histamine_serotonin_button.grid(row=2, column=0)
        #Import waveform panel.
        self.import_button = self.parent_class.gui_methods.get_button_object(self.import_waveform_frame, self.import_waveform_changed, 2, 10, 'Import', [0,0,2,1,0,0], '#3f51b5', 'white')
        #Waveform graph.
        self.figure, self.axes, self.line, self.canvas, self.plot_widget = self.parent_class.gui_methods.init_XY_graph(self.main_frame, [5,5], 100, [0,1,1,1,10,10], [], [],  2, 'black', 'Voltage (V)', 'Time (s)', 8)

        #Apply and close buttons
        self.apply_button = self.parent_class.gui_methods.get_button_object(self.apply_frame, self.apply_changes_pushed, 2, 10, 'Apply', [0,0,1,1,0,0], '#3f51b5', 'white')
        self.import_button = self.parent_class.gui_methods.get_button_object(self.apply_frame, self.close_button_pushed, 2, 10, 'Close', [0,1,1,1,0,0], '#3f51b5', 'white')
        #Initialise dopamine waveform.
        self.saved_waveform_changed()

    def refresh_waveform(self):
        if self.tab_frame.index('current') == 0:
            self.saved_waveform_changed()
        elif self.tab_frame.index('current') == 1:
            self.edit_waveform_changed()
        elif self.tab_frame.index('current') == 2:
            self.coordinates_waveform_changed()


    def edit_waveform_changed(self):
        low = float(self.low_potential_input.get())
        high = float(self.high_potential_input.get())
        rate = float(self.scan_rate_input.get())
        samples = int(np.abs((high-low)/rate)*self.parent_class.acquisition.frequency)
        rolling = int(float(self.phase_shift_input.get())*(2/100)*samples)
        self.voltage_array = np.roll(np.append(np.linspace(low, high, samples), np.linspace(high, low, samples)), rolling)
        self.time_array = np.linspace(0, len(self.voltage_array)/self.parent_class.acquisition.frequency, len(self.voltage_array))
        self.regraph_waveform()

    def coordinates_waveform_changed(self):
        self.voltage_array = []
        self.time_array = []
        self.coordinates_array = [[float(self.list_of_coordinates.item(child)["values"][0]), float(self.list_of_coordinates.item(child)["values"][1])] for child in self.list_of_coordinates.get_children()]
        self.get_array_from_coordinates()
        self.regraph_waveform()


    def export_waveform(self):
        file = tk.filedialog.asksaveasfile(filetypes = [('Text Document', '*.txt')])
        for i in range(0, len(self.voltage_array)):
            file.write(str(self.time_array[i])+'\t'+str(self.voltage_array[i])+'\n')
        file.close()



    def regraph_waveform(self):
        self.line[0].set_data(self.time_array, self.voltage_array)
        self.axes.relim()
        self.axes.autoscale_view()
        self.canvas.draw()
        self.canvas.flush_events()

    def add_point_to_table(self):
        self.point_counter = len(self.list_of_coordinates.get_children())
        self.list_of_coordinates.insert("", self.point_counter, self.point_counter, text=str(self.point_counter), values=(self.time_input.get(), self.voltage_input.get()))
        self.point_counter = self.point_counter + 1

    def remove_point_of_table(self):
        self.point_counter = len(self.list_of_coordinates.get_children())
        self.list_of_coordinates.delete(self.point_counter-1)
        self.point_counter = self.point_counter - 1


    def saved_waveform_changed(self):
        if self.saved_waveform_variable.get() == 'DA':
            self.coordinates_array = self.parent_class.waveform_settings.dopamine
        elif self.saved_waveform_variable.get() == '5-HT':
            self.coordinates_array = self.parent_class.waveform_settings.serotonin
        elif self.saved_waveform_variable.get() == 'HA/5-HT':
            self.coordinates_array = self.parent_class.waveform_settings.histamine_serotonin
        self.voltage_array = []
        self.time_array = []
        self.get_array_from_coordinates()
        self.regraph_waveform()


    def import_waveform_changed(self):
        file = tk.filedialog.askopenfile(filetypes = [('Text Document', '*.txt')])
        if file:
            data = [row.split('\t') for row in file.read().split('\n')]
            self.voltage_array = []
            self.time_array = []
            for row in data:
                if len(row)==2:
                    self.time_array.append(float(row[0]))
                    self.voltage_array.append(float(row[1]))
            file.close()
            self.regraph_waveform()

    def apply_changes_pushed(self):
        self.parent_class.waveform_settings.voltage_array = self.voltage_array
        self.parent_class.waveform_settings.time_array = self.time_array
        self.parent_class.waveform_settings.regraph_waveform()

    def close_button_pushed(self):
        self.master.destroy()

    def get_array_from_coordinates(self):
        self.point_counter = len(self.coordinates_array)
        for i in range(1, self.point_counter):
            samples = int(np.abs(self.parent_class.acquisition.frequency*(self.coordinates_array[i][0]-self.coordinates_array[i-1][0])))
            self.time_array = np.append(self.time_array, np.linspace(self.coordinates_array[i-1][0], self.coordinates_array[i][0], samples))
            self.voltage_array = np.append(self.voltage_array, np.linspace(self.coordinates_array[i-1][1], self.coordinates_array[i][1], samples))
