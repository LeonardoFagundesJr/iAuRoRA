
#---
def plotUAVcontrolSignals(df,plt):  
    ## - Plot the Control Signals
    fig, axs = plt.subplots(2,2, sharex=True)

    fig.suptitle("Control Signals (Executed by the Drone)")

    # ---------- u_\theta
    axs[0,0].plot(df['time'], df['A.pSCU[0]'])

    axs[0,0].set(ylabel=r'$u_{\theta}~$ [rad]')
    axs[0,0].grid(True)
    axs[0,0].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['A.pSCU[0]'])-0.025, max(df['A.pSCU[0]'])+0.025))

    # ---------- u_\phi
    axs[0,1].plot(df['time'], df['U[1]'])

    axs[0,1].set(ylabel=r'$u_{\phi}~$ [rad]')
    axs[0,1].grid(True)
    axs[0,1].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['U[1]'])-0.025, max(df['U[1]'])+0.025))

    # ---------- u_{\Dot{\psi}}
    axs[1,0].plot(df['time'], df['U[2]'])

    axs[1,0].set(xlabel='time [$s$]', ylabel='$u_{\dot{\psi}}~$ [rad/s]')
    axs[1,0].grid(True)
    axs[1,0].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['U[2]'])-0.025, max(df['U[2]'])+0.025))


    # ---------- u_{\Dot{z}}
    axs[1,1].plot(df['time'], df['U[3]'])

    axs[1,1].set(xlabel='time [$s$]', ylabel='$u_{z}~$ [m/s]')
    axs[1,1].grid(True)
    axs[1,1].set(xlim=(min(df['time']), max(df['time'])), 
          ylim=(min(df['U[3]'])-0.025, max(df['U[3]'])+0.025))


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
    plt.rcParams['figure.figsize'] = (22,8)
    plt.rc('font', size=26)
    plt.rc('axes', titlesize=25) 

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')

    print('\n')
    plt.show()

    return fig
