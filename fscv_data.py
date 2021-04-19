from libraries import *
from fscv_classes import FSCV_3D_ARRAY
class FSCV_DATA:
    def __init__(self, parent_class, z_units, y_units, x_units, z_label, y_label, x_label, z_min, z_max, name, array):
        self.parent_class = parent_class
        self.frequency = None
        self.cycling_frequency = None
        self.name_of_file = None
        self.current = FSCV_3D_ARRAY(z_units, y_units, x_units, z_label, y_label, x_label, name, array)
        #Color plot setting parameters.
        self.color_palette = self.parent_class.plot_configuration.custom
        self.color_palette_name = 'Custom'
        self.color_upper_bound = z_max
        self.color_lower_bound = z_min
        #Figure variables.
        self.figure = None
        self.axes = None
        self.image_matrix = None
        self.canvas = None
        self.plot_widget = None
        self.toolbar = None
        self.colorbar = None

    def init_color_plot(self, macro, size_x, size_y, dpi, fontsize, position):
        self.figure = Figure(figsize=(size_x, size_y), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_ylabel(self.current.y_label+' ('+self.current.y_units+')', fontsize=fontsize)
        self.axes.set_xlabel(self.current.x_label+' ('+self.current.x_units+')', fontsize=fontsize)
        self.axes.tick_params(axis='both', labelsize=fontsize)
        self.image_matrix = self.axes.imshow(self.current.array, cmap=self.color_palette, vmin=self.color_lower_bound, vmax=self.color_upper_bound)
        divider = make_axes_locatable(self.axes)
        cax2 = divider.append_axes("right", size="5%", pad=0.05)
        self.colorbar = self.figure.colorbar(self.image_matrix, cax=cax2)
        self.colorbar.ax.tick_params(labelsize=fontsize)
        self.canvas = FigureCanvasTkAgg(self.figure, master=macro)
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.parent_class.color_plot_toolbar_frame)
        self.plot_widget = self.canvas.get_tk_widget()
        self.plot_widget.grid(row=position[0], column=position[1], rowspan=position[2], columnspan=position[3], padx=position[4], pady=position[5])

    def refresh_color_plot(self):
        self.image_matrix.set_data(self.current.array)
        self.axes.relim()
        self.axes.autoscale_view()
        self.canvas.draw()
        self.canvas.flush_events()
        
    def change_color_palette(self):
        self.image_matrix.set_cmap(self.color_palette)
        self.image_matrix.set_clim(vmin=self.color_lower_bound, vmax=self.color_upper_bound)
        self.canvas.draw()
        self.canvas.flush_events()
