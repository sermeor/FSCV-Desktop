from libraries import *
class ACQUISITION_SETTINGS:
    def __init__(self, parent_class):
        self.cycling_frequency = 10
        self.frequency = 150000
        self.total_acquisition_time = 30
        self.gain = 500
        self.waveform_multiplier = 1
        self.average_cvs_background_subtraction = 10
