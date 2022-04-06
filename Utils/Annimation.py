
#---
def updateCurve(w,ax):
    
    global i,df
    
#     ax.clear()

#     i += 8

    ax.set_xlim3d([-2.5, 2.5])
    ax.set_xlabel('$x~$[m]',labelpad=10)

    ax.set_ylim3d([-2.5, 2.5])
    ax.set_ylabel('$y~$[m]',labelpad=10)

    ax.set_zlim3d([0.0, 2.5])
    ax.set_zlabel('$z~$[m]',labelpad=10)

    ax.set_title('Route Performed by the ArDrone')
    
#     if i > 0 and i < 450:
#         ax.scatter3D(df['A.pPosXd[0]'][[0]], df['Xd[1]'][[0]],
#                   df['Xd[2]'][[0]], marker='o', alpha = 0.5, color='red')        
#     elif i > 450 and i < 900:
#         ax.scatter3D(df['A.pPosXd[0]'][[0,500]], df['Xd[1]'][[0,500]],
#                   df['Xd[2]'][[0,500]], marker='o', alpha = 0.5, color='red')
#     elif i > 900 and i < 1350:
#         ax.scatter3D(df['A.pPosXd[0]'][[0,500,1000]], df['Xd[1]'][[0,500,1000]],
#                   df['Xd[2]'][[0,500,1000]], marker='o', alpha = 0.5, color='red')
#     else:
#         ax.scatter3D(df['A.pPosXd[0]'][[0,500,1000,1500]], df['Xd[1]'][[0,500,1000,1500]],
#                   df['Xd[2]'][[0,500,1000,1500]], marker='o', alpha = 0.5, color='red')        
    

#     ax.plot3D(df['A.pPosX[0]'][0:i], df['X[1]'][0:i], df['X[2]'][0:i], label='Position')

    ax.plot3D(df['A.pPosX[0]'][w], df['X[1]'][w], df['X[2]'][w], label='Position')

    ax.legend(['$\mathbf{x}$','$\mathbf{x_d}$'],loc='center right', bbox_to_anchor=(1.05, 0.5))

    fig = plt.gcf()

    return fig
