import matplotlib
import matplotlib.pyplot as plt

# matplotlib.rcParams['mathtext.fontset'] = 'stix'
# matplotlib.rcParams['font.family'] = 'STIXGeneral'
# plt.rcParams['text.usetex'] = True
# plt.rcParams['text.latex.unicode'] = True
# matplotlib.rcParams['text.usetex'] = True
# matplotlib.rcParams['text.latex.unicode'] = True

page_width = 15.5 # cm
page_width = page_width*0.3937 # inches

standard_figure_width = 0.7*page_width
standard_figure_height = 0.7*standard_figure_width

large_figure_width = 0.95/0.7*standard_figure_width
large_figure_height = 0.7*large_figure_width

nb_pixels = 1000
dpi_picture_standart = 1000/ standard_figure_width
dpi_picture_large = 1000/ large_figure_width


matplotlib.rcParams['font.size'] = 12

def label_axes( axes_list, letter_distance = ( 5, -5 ), bbox = False, letter_index = 0 ) :

    letters = 'abcdefghijklmnopqrstuvwxyz'
     # points

    if bbox :
        bbox = dict( boxstyle = "round, pad=.2", fc = 'white', ec = 'none', alpha = .7 )
    else :
        bbox = dict( boxstyle = "round, pad=.2", fc = 'none', ec = 'none' )

    for ax in axes_list :

        zorder = max( [ _.zorder for _ in ax.get_children() ] )

        ax.annotate( letters[ letter_index ],
            xy = ( 0, 1 ), xycoords = 'axes fraction',
            xytext = letter_distance, textcoords = 'offset points',
            ha = 'left', va = 'top',
            # fontsize = panel_label_font_size, fontweight = 'bold',
            bbox = bbox,
            zorder = zorder + 1,
            )

        letter_index += 1
