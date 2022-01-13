
# --
def graphicsConfig(plt):

    SMALL_SIZE = 16
    MEDIUM_SIZE = 18
    BIGGER_SIZE = 22

    plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=MEDIUM_SIZE)   # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE)   # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

    # The axes attributes need to be set before the call to subplot
    plt.rcParams.update({
      "grid.color": "0.5",
      "grid.linestyle": "--",
      "grid.linewidth": 0.5,
      "lines.linewidth": 1,
      "lines.color": "g"})

    plt.rcParams.update({
      "text.usetex": True,
      "font.family": "sans-serif",
      "font.sans-serif": ["Helvetica"]})


    # set font of all elements to size:
    plt.rc('axes', titlesize = 25) 

    plt.rcParams['figure.figsize'] = (8,6)

    plt.rc('font', size = 20)

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    return None
