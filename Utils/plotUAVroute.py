

#---
def plotUAVroute(df):
    ## - Plot the Robot Position

    fig, axs = plt.subplots(3, sharex=True)

    fig.suptitle("Robot Position")

    # ---------- x
    axs[0].plot(df['time'], df['A.pPosXd[0]'])
    axs[0].plot(df['time'], df['A.pPosX[0]'], color='red')

    axs[0].set(ylabel='$\widetilde{x}~$ [m]')
    axs[0].legend(['$x_d$','$x$'],loc='upper right', bbox_to_anchor=(1.15, 1))
    axs[0].grid(True)
    axs[0].set_yticks([-2.0,-1.0,0,1.0,2.0])
    axs[0].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['A.pPosX[0]'])-0.25, max(df['A.pPosX[0]'])+0.25))

    # ---------- y
    axs[1].plot(df['time'], df['Xd[1]'])
    axs[1].plot(df['time'], df['X[1]'], color='red')

    axs[1].set(ylabel='$\widetilde{y}~$ [m]')
    axs[1].legend(['$y_d$','$y$'],loc='upper right', bbox_to_anchor=(1.15, 1))
    axs[1].grid(True)
    axs[1].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['X[1]'])-0.25, max(df['X[1]'])+0.25))

    # ---------- z
    axs[2].plot(df['time'], df['Xd[2]'])
    axs[2].plot(df['time'], df['X[2]'], color='red')

    axs[2].set(xlabel='time [$s$]', ylabel='$\widetilde{z}~$ [m]')
    axs[2].legend(['$z_d$','$z$'],loc='upper right', bbox_to_anchor=(1.15, 1))
    axs[2].grid(True)
    axs[2].set_yticks([-2.0,-1.0,0,1.0,2.0])
    axs[2].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['X[2]'])-0.25, max(df['X[2]'])+0.25))

    Fig = plt.gcf()

    plt.show()

    # the axes attributes need to be set before the call to subplot
    plt.rcParams.update({
        "grid.color": "0.5",
        "grid.linestyle": "--",
        "grid.linewidth": 0.25,
        "lines.linewidth": 1,
        "lines.color": "g"})

    plt.rcParams.update({
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": ["Helvetica"]})

    # set font of all elements to size 15
    plt.rcParams['figure.figsize'] = (10,8)
    plt.rc('font', size=22)
    plt.rc('axes', titlesize=25) 

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    print('\n')
    plt.show()

    return fig