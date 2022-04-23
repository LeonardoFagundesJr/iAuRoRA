#---
def plotUAVangularVel(df,plt):
    ## - Plot the Linear & Angular Velocities

    fig, axs = plt.subplots(3, sharex=True)

    fig.suptitle("Robots' Angular Velocities")

    # ---------- \phi
    axs[0].plot(df['time'], df['Xd[9]'])
    axs[0].plot(df['time'], df['X[9]'], color='red')

    axs[0].set(ylabel=r'$\dot{\widetilde{\phi}}~$ [rad/s]')
    axs[0].legend(['$\dot{\phi}_d$','$\dot{\phi}$'],loc='upper right', bbox_to_anchor=(1.20, 1))
    axs[0].grid(True)
    axs[0].set_yticks([-2,-1,0,1,2])
    axs[0].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['Xd[9]'])-0.25, max(df['Xd[9]'])+0.25))


    # zoomed a portion of image Version01
    axZoom = plt.axes([.75, .855, .125, .1])                        # [left, bottom, width, height]
    plt.plot(df['time'][1275:1650], df['Xd[9]'][1275:1650])
    plt.plot(df['time'][1275:1650], df['X[9]'][1275:1650], color='red')
    # plt.setp(axZoom, xticks=[], yticks=[])
    for label in (axZoom.get_xticklabels() + axZoom.get_yticklabels()): label.set_fontsize(15)

    x1, x2, y1, y2 = df['time'][1275], df['time'][1650], min([min(df['Xd[9]'][1275:1650]),min(df['X[9]'][1275:1650])])-0.125, max([max(df['Xd[9]'][1275:1650]),max(df['X[9]'][1275:1650])])+0.125
    axZoom.set_xlim(x1, x2)
    axZoom.set_ylim(y1, y2)
    axs[0].indicate_inset_zoom(axZoom, edgecolor="black", transform=None)

    ### --- Issso se chama gambiarra!
    x1, x2, y1, y2 = df['time'][1275], df['time'][1650], min([min(df['Xd[9]'][1275:1650]),min(df['X[9]'][1275:1650])]), max([max(df['Xd[9]'][1275:1650]),max(df['X[9]'][1275:1650])])
    axZoom.set_xlim(x1, x2)
    axZoom.set_ylim(y1, y2)

    # zoomed a portion of image Version02
    # inset axes....
    # axins = axs[0].inset_axes([.80, .855, .15, .5])
    # axins.plot(df['time'][1275:1650], df['Xd[9]'][1275:1650])
    # axins.plot(df['time'][1275:1650], df['X[9]'][1275:1650], color='red')

    # # sub region of the original image
    # x1, x2, y1, y2 = df['time'][1275], df['time'][1650], min([min(df['Xd[9]'][1275:1650]),min(df['X[9]'][1275:1650])])-0.125, max([max(df['Xd[9]'][1275:1650]),max(df['X[9]'][1275:1650])])+0.125

    # axins.set_xlim(x1, x2)
    # axins.set_ylim(y1, y2)
    # # axins.set_xticklabels('')
    # # axins.set_yticklabels('')

    # axs[0].indicate_inset_zoom(axins, edgecolor="black")
    # for label in (axins.get_xticklabels() + axins.get_yticklabels()): label.set_fontsize(15)




    # ---------- \theta
    axs[1].plot(df['time'], df['Xd[10]'])
    axs[1].plot(df['time'], df['X[10]'], color='red')

    axs[1].set(ylabel=r'$\dot{\widetilde{\theta}}~$ [rad/s]')
    axs[1].legend([r'$\dot{\theta}_d$',r'$\dot{\theta}$'],loc='upper right', bbox_to_anchor=(1.2, 1))
    axs[1].grid(True)
    axs[1].set_yticks([-2,-1,0,1,2])
    axs[1].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['Xd[10]'])-0.25, max(df['Xd[10]'])+0.25))

    # ---------- \psi
    axs[2].plot(df['time'], df['Xd[11]'])
    axs[2].plot(df['time'], df['X[11]'], color='red')

    axs[2].set(xlabel='time [$s$]', ylabel='$\dot{\widetilde{\psi}}~$ [rad/s]')
    axs[2].legend(['$\dot{\psi}_d$','$\dot{\psi}$'],loc='upper right', bbox_to_anchor=(1.2, 1))
    axs[2].grid(True)
    axs[2].set_yticks([-0.2,0,0.2])
    axs[2].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['X[11]'])-0.025, max(df['X[11]'])+0.025))


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



    print('\n\n')
    
    print('\n')
    plt.show()

    return fig