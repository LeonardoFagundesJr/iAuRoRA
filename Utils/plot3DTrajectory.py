

#---
def plot3DTrajectory(df,plt):
    fig = plt.figure(facecolor='w')
    ax = fig.gca(projection='3d', adjustable='box', facecolor=[1, 1, 1])

    ax.plot3D(df['A.pPosX[0]'], df['X[1]'], df['X[2]'], label='Position')
    ax.scatter3D(df['A.pPosXd[0]'][[0,500,1000,1500]], df['Xd[1]'][[0,500,1000,1500]],
                df['Xd[2]'][[0,500,1000,1500]], marker='o', alpha = 0.5, color='red')

    ax.set_xticklabels([-2,-1,0,1,2],rotation=0, ha='right')
    ax.set_yticklabels([-2,-1,0,1,2],rotation=0, ha='center')
    ax.set_zlabel('$z~$[m]',rotation=-90,labelpad=10,rotation_mode='anchor')
    ax.set_ylabel('$y~$[m]',labelpad=10, ha='left')
    ax.set_xlabel('$x~$[m]',labelpad=10, ha='left')

    # ax.set_title('Route Performed by the ArDrone')
    fig.suptitle('Route Performed by the ArDrone')
    ax.legend(['$\mathbf{x}$','$\mathbf{x_d}$'],loc='center right', bbox_to_anchor=(1.05, 0.5))
    ax.set_xticks([-2.0,-1.0,0,1.0,2.0])
    ax.set_yticks([-2.0,-1.0,0,1.0,2.0])
    ax.set_zticks([0,1.0,2.0,3.0,4.0])
    ax.set(xlim=(-2.5, 2.5), ylim=(-2.5, 2.5), zlim=(1.5, 2))

    # rotate the axes and update
    # ax.view_init(35, -125)
    ax.view_init(20, 235)
    plt.draw()
    
    plt.rcParams['figure.figsize'] = (8,6)    # Largura, Altura

    # -----
    plt.tight_layout()

    ax.set_xlim3d([-2.5, 2.5])
    ax.set_xlabel('$x~$[m]',labelpad=10)

    ax.set_ylim3d([-2.5, 2.5])
    ax.set_ylabel('$y~$[m]',labelpad=10)

    ax.set_zlim3d([0.0, 2.5])
    ax.set_zlabel('$z~$[m]',labelpad=10)

    print('\n')

    plt.show()

    plt.pause(2)

    # # rotate the axes and update
    # for angle in range(0, 360):
    #     ax.view_init(30, angle)
    #     plt.draw()
    #     plt.pause(.001)

    return fig



# -------------- Plot Desired Trajectory:
#---
def plot3DTrajectoryTracking(df,plt):
    fig = plt.figure(facecolor='w')
    ax = fig.gca(projection='3d', adjustable='box', facecolor=[1, 1, 1])

    ax.plot3D(df['A.pPosX[0]'], df['X[1]'], df['X[2]'], label='Position')
    ax.plot3D(df['A.pPosXd[0]'], df['Xd[1]'], df['Xd[2]'], '--', alpha = 0.5, color='red')

    ax.set_zlabel('$z~$[m]',rotation=-90,labelpad=10,rotation_mode='anchor')
    ax.set_ylabel('$y~$[m]',labelpad=10, ha='left')
    ax.set_xlabel('$x~$[m]',labelpad=10, ha='left')

    # ax.set_title('Route Performed by the ArDrone')
    fig.suptitle('Route Performed by the ArDrone')
    ax.legend(['$\mathbf{x}$','$\mathbf{x_d}$'],loc='center right', bbox_to_anchor=(1.05, 0.5))

    # rotate the axes and update
    ax.view_init(35, -125)
    plt.draw()
    
    plt.rcParams['figure.figsize'] = (10,8)    # Largura, Altura

    # -----
    plt.tight_layout()

    ax.set_xlim3d([-1.5, 1.5])

    ax.set_ylim3d([-1.5, 1.5])

    ax.set_zlim3d([0.0, 2.5])

    print('\n')

    plt.show()

    return fig
