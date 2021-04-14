import matplotlib.colors as mcolors

class PLOT_SETTINGS:
    def __init__(self):
        #Custom colormaps.
        self.custom = self.get_continuous_cmap(['#0000f0', '#000227', '#f5d501', '#a86200', '#4c0245', '#00b688', '#008a1e', '#01f801'],[0, 0.2478, 0.3805, 0.6555, 0.701, 0.7603, 0.7779, 1])
        self.ibm = self.get_continuous_cmap(['#648FFF', '#785EF0', '#DC267F', '#FE6100', '#FFB000'],[0, 0.25, 0.50, 0.75, 1])
        self.wang = self.get_continuous_cmap(['#009E73', '#F0E442', '#0072B2', '#D55E00', '#CC79A7'],[0, 0.25, 0.50, 0.75, 1])
        self.grays = 'gray'

    def get_continuous_cmap(self, hex_list, float_list=None):
        rgb_list = [self.rgb_to_dec(self.hex_to_rgb(i)) for i in hex_list]
        if float_list:
            pass
        else:
            float_list = list(np.linspace(0,1,len(rgb_list))) #Linear colormap.

        cdict = dict()
        for num, col in enumerate(['red', 'green', 'blue']):
            col_list = [[float_list[i], rgb_list[i][num], rgb_list[i][num]] for i in range(len(float_list))]
            cdict[col] = col_list
        cmp = mcolors.LinearSegmentedColormap('my_cmp', segmentdata=cdict, N=256)
        return cmp

    def hex_to_rgb(self, value):
        value = value.strip("#") # removes hash symbol if present
        lv = len(value)
        return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    def rgb_to_dec(self, value):
        return [v/256 for v in value]
