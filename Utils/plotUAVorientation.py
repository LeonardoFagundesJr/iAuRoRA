#---
def plotUAVorientation(df,plt):
    ## - Plot the Robot Position
    import numpy as np
    
    fig, axs = plt.subplots(3, sharex=True)

    fig.suptitle("Robot Orientation")

    # ---------- x
    axs[0].plot(df['time'], df['Xd[3]']*180/np.pi)
    axs[0].plot(df['time'], df['X[3]']*180/np.pi, color='red')

    axs[0].set(ylabel='$\widetilde{\phi}~$ [$^\circ$]')
    axs[0].legend(['$\phi_d$','$\phi$'],loc='upper right', bbox_to_anchor=(1.10, 1))
    axs[0].grid(True)
    axs[0].set_yticks([-4.0,-2.0,0,2.0,4.0])
    axs[0].set(xlim=(min(df['time']), max(df['time'])), 
        ylim=(min(df['Xd[3]']*180/np.pi)-0.25, max(df['Xd[3]']*180/np.pi)+0.25))

    # ---------- y
    axs[1].plot(df['time'], df['Xd[4]']*180/np.pi)
    axs[1].plot(df['time'], df['X[4]']*180/np.pi, color='red')

    axs[1].set(ylabel=r'$\widetilde{\theta}~$ [$^\circ$]')
    axs[1].legend([r'$\theta_d$',r'$\theta$'],loc='upper right', bbox_to_anchor=(1.10, 1))
    axs[1].grid(True)
    axs[1].set_yticks([-4.0,-2.0,0,2.0,4.0])
    axs[1].set(xlim=(min(df['time']), max(df['time'])), 
        ylim=(min(df['Xd[4]']*180/np.pi)-0.5, max(df['Xd[4]']*180/np.pi)+0.5))

    # ---------- z
    axs[2].plot(df['time'], df['Xd[5]']*180/np.pi)
    axs[2].plot(df['time'], df['X[5]']*180/np.pi, color='red')

    axs[2].set(xlabel='time [$s$]', ylabel='$\widetilde{\psi}~$ [$^\circ$]')
    axs[2].legend(['$\psi_d$','$\psi$'],loc='upper right', bbox_to_anchor=(1.10, 1))
    axs[2].grid(True)
    axs[2].set_yticks([0,15,30,45])
    axs[2].set(xlim=(min(df['time']), max(df['time'])), 
        ylim=(min(df['Xd[5]']*180/np.pi)-5, max(df['Xd[5]']*180/np.pi)+5))


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