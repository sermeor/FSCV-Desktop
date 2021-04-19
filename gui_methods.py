from libraries import *
class GUI_METHODS:
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

    def init_XY_graph(self, macro, size, dpi, position, array_x, array_y, thickness, color, ylabel, xlabel, fontsize):
        figure = Figure(figsize=(size[0], size[1]), dpi=dpi)
        axes = figure.add_subplot(111)
        axes.set_ylabel(ylabel, fontsize=fontsize)
        axes.set_xlabel(xlabel, fontsize=fontsize)
        axes.tick_params(axis='both', labelsize=fontsize)
        line = axes.plot(array_x, array_y, marker='.', color=color, linewidth=thickness)
        axes.grid()
        canvas = FigureCanvasTkAgg(figure, master=macro)
        plot_widget = canvas.get_tk_widget()
        plot_widget.grid(row=position[0], column=position[1], rowspan=position[2], columnspan=position[3], padx=position[4], pady=position[5])
        return figure, axes, line, canvas, plot_widget
