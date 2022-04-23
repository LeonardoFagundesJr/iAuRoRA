#---
def plotUAVlinearVel(df,plt):
    ## - Plot the Linear Velocities
    #--------------//--------------#

    fig, axs = plt.subplots(3, sharex=True)

    fig.suptitle("Robots' Linear Velocities")

    # ---------- x
    axs[0].plot(df['time'], df['Xd[6]'])
    axs[0].plot(df['time'], df['X[6]'], color='red')

    axs[0].set(ylabel='$\dot{\widetilde{x}}~$ [m/s]')
    axs[0].legend(['$\dot{x}_d$','$\dot{x}$'],loc='upper right', bbox_to_anchor=(1.20, 1))
    axs[0].grid(True)
    axs[0].set_yticks([-0.6,-0.4,-0.2,-0.1,0,0.1,0.2,0.4,0.6])
    axs[0].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['X[6]'])-0.025, max(df['X[6]'])+0.025))

    # ---------- y
    axs[1].plot(df['time'], df['Xd[7]'])
    axs[1].plot(df['time'], df['X[7]'], color='red')

    axs[1].set(ylabel=r'$\dot{\widetilde{y}}~$ [m/s]')
    axs[1].legend([r'$\dot{y}_d$',r'$\dot{y}$'],loc='upper right', bbox_to_anchor=(1.2, 1))
    axs[1].grid(True)
    axs[1].set_yticks([-0.6,-0.4,-0.2,-0.1,0,0.1,0.2,0.4,0.6])
    axs[1].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['X[7]'])-0.025, max(df['X[7]'])+0.025))

    # ---------- z
    axs[2].plot(df['time'], df['Xd[8]'])
    axs[2].plot(df['time'], df['X[8]'], color='red')

    axs[2].set(xlabel='time [$s$]', ylabel='$\dot{\widetilde{z}}~$ [m/s]')
    axs[2].legend(['$\dot{z}_d$','$\dot{z}$'],loc='upper right', bbox_to_anchor=(1.2, 1))
    axs[2].grid(True)
    axs[2].set_yticks([-0.6,-0.4,-0.2,0,0.2,0.4,0.6])
    axs[2].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['X[8]'])-0.025, max(df['X[8]'])+0.025))


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
    plt.rc('font', size=20)
    plt.rc('axes', titlesize=25) 

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    print('\n')
    plt.show()

    return fig
