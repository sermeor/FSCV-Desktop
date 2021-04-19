from libraries import *
class OSCILLOSCOPE_WINDOW:
    def __init__(self, parent_class):
        self.master = tk.Toplevel(parent_class.master,  bg='white')
        self.master.title('Oscilloscope')
        self.master.resizable(False, False)
        self.master.transient(parent_class.master)
        self.master.grab_set()
        self.parent_class = parent_class
        self.main_frame = tk.Frame(self.master, bg='white')
        self.main_frame.grid(row=0, column=0, padx=10, pady=10)

        self.control_frame = tk.Frame(self.master, bg='white')
        self.control_frame.grid(row=0, column=0)

        self.graph_frame = tk.Frame(self.master, bg='white')
        self.graph_frame.grid(row=0, column=1)

        self.oscilloscope_graph = self.parent_class.gui_methods.init_XY_graph(self.graph_frame, [5,5], 100, [0,1,1,1,10,10], [], [],  2, 'black', 'Voltage (V)', 'Time (s)', 8)
