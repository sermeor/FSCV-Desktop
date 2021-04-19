from libraries import *
class WAVEFORM_SETTINGS:
    def __init__(self, parent_class):
        #Predefined waveforms.
        self.dopamine = [[0, -0.4], [0.00425, 1.3], [0.0085, -0.4]]
        self.serotonin = [[0, 0.2], [0.0008, 1], [0.0019, -0.1], [0.0022, 0.2]]
        self.histamine_serotonin = [[0, -0.51], [0.000318, -0.7] ,[0.003316, 1.1], [0.006, -0.51]]

        self.parent_class = parent_class
        #Waveform variables for edit waveform.
        self.scan_rate = 400
        self.low_potential = -0.4
        self.high_potential = 1.3
        self.phase_shift = 0
        #Waveform variables for coorinates waveform and initialization.
        self.voltage_array = []
        self.time_array = []
        for i in range(1, len(self.dopamine)):
            samples = int(np.abs(self.parent_class.acquisition.frequency*(self.dopamine[i][0]-self.dopamine[i-1][0])))
            self.time_array = np.append(self.time_array, np.linspace(self.dopamine[i-1][0], self.dopamine[i][0], samples))
            self.voltage_array = np.append(self.voltage_array, np.linspace(self.dopamine[i-1][1], self.dopamine[i][1], samples))

        #Variables of XY figure in main window.
        self.figure, self.axes, self.line, self.canvas, self.plot_widget = self.parent_class.gui_methods.init_XY_graph(self.parent_class.voltage_XY_frame, [5,5], 100, [0,1,1,1,10,10], self.time_array, self.voltage_array, 2, 'black', 'Voltage (V)', 'Time (s)', 8)


    def regraph_waveform(self):
        self.line[0].set_data(self.time_array, self.voltage_array)
        self.axes.relim()
        self.axes.autoscale_view()
        self.canvas.draw()
        self.canvas.flush_events()
