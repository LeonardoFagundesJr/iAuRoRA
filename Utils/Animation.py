# Função para gerar a Figura 3D onde será realizada a animação:

def anim3Dplot(plt, df, dTAnim):
    
    import numpy as np
    import math

#     global pxAnim, pyAnim, pzAnim, pxdAnim, pydAnim, pzAnim, phiAnim, thetaAnim, psiAnim

    dT = df['time'].iloc[-1]/(len(df)-1)      # Tempo de amostragem do robô [s]
    samples = math.ceil(dTAnim/dT)            # taxa de amostragem do novo vetor

    pxAnim = df['A.pPosX[0]'][::samples]      # vetor x com novo numero de amostras
    pyAnim = df['X[1]'][::samples]            # vetor y com novo numero de amostras
    pzAnim = df['X[2]'][::samples]            # vetor z com novo numero de amostras

    pxdAnim = df['A.pPosXd[0]'][::samples]    # vetor x_d com novo numero de amostras
    pydAnim = df['Xd[1]'][::samples]          # vetor y_d com novo numero de amostras
    pzdAnim = df['Xd[2]'][::samples]          # vetor z_d com novo numero de amostras

    phiAnim = df['X[3]'][::samples]           # vetor PHI com novo numero de amostras
    thetaAnim = df['X[4]'][::samples]         # vetor THETA com novo numero de amostras
    psiAnim = df['X[5]'][::samples]           # vetor PSI com novo numero de amostras


    plt.rc('axes', axisbelow=True) # Manda o grid para trás
    plt.rcParams['animation.embed_limit'] = 2**128

    # Attaching 3D axis to the figure
    fig = plt.figure(figsize=(8,6))
    ax = fig.add_subplot(projection="3d", adjustable='box')

    # Setting the axes properties
    ax.set_title('Route Performed by the ArDrone')
    ax.view_init(35, -125)
    plt.draw()

    # the axes attributes need to be set before the call to subplot
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


    #set font of all elements to size 15


    plt.rc('axes', titlesize=25) 

    plt.rcParams['figure.figsize'] = (10,10)

    plt.rc('font', size=20)

    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')


    # -----
    plt.tight_layout()

    # set_axes_equal(ax)

    ax.set_xlim3d([-2.5, 2.5])
    ax.set_xlabel('$x~$[m]',labelpad=10)

    ax.set_ylim3d([-2.5, 2.5])
    ax.set_ylabel('$y~$[m]',labelpad=10)

    ax.set_zlim3d([0.0, 2.5])
    ax.set_zlabel('$z~$[m]',labelpad=10)


    ax.text(0, 0, 4.5, 'Route Performed by the ArDrone', ha='center', size=20)

    # create objects that will change in the animation. These are
    # initially empty, and will be given new values for each frame
    # in the animation.
    txt_title = ax.text(0, 0, 3.25, '', ha='center', size=18)

    print('\n')

    plt.close()


    # Ploting data base:
    dataSet = np.array([pxAnim, pyAnim, pzAnim])  # This would be the z-axis 
    dataSetd = np.array([pxdAnim, pydAnim, pzdAnim])  # This would be the z-axis 
    
    uav = ax.plot(dataSet[0], dataSet[1], dataSet[2], 'o', markersize=10, color='k', alpha=0.5,label='$\langle\mathrm{UAV}\\rangle$')[0] # inicializa o centro do drone
    route = ax.plot(dataSet[0], dataSet[1], dataSet[2], lw=2, color='g', alpha=0.5, label=r'$\mathbf{x}$')[0] # inicializa a rota do drone
    xd = ax.plot(dataSetd[0], dataSetd[1], dataSetd[2], 'x', markersize=12.5, lw=2, alpha = 0.5, color='red', label=r'$\mathbf{x}_d$')[0]

    ax.legend(loc='center right', bbox_to_anchor=(1.05, 0.5))

    return fig, ax, txt_title, uav, route, xd, dataSet, dataSetd



# Inicializa a funcao de animacao: plota o drone e o fundo 
def init():

    return uav, route, xd,


# Função que gera a animação: 

#---
def updateCurve(w, tempo, dataSet, dataSetd, txt_title, dTAnim):
    global tempo, dataSet, dataSetd, txt_title
    # 'w' is the frame
    
    txt_title.set_text("time: %.2f [seg], {\em frame}: %2.0f"%(tempo,w) )

    # Update the robot position:
    uav.set_data(dataSet[0:2, w])    
    uav.set_3d_properties(dataSet[2, w]) 

    # Update the robot trajectory:
    route.set_data(dataSet[0:2, :w])    
    route.set_3d_properties(dataSet[2, :w])

    # Update the robot desired trajectory:
    xd.set_data(dataSetd[0:2, :w])    
    xd.set_3d_properties(dataSetd[2, :w])

    plt.draw()
    
    tempo += (dTAnim)
    plt.draw()

    return uav, route, xd,


# Save Animation as video file
def saveAnimation(anim, fileName, dTAnim, dpi):
    import os

    if not(os.path.isdir('../content/Animation/')):
        os.mkdir('../content/Animation/')

    f = os.path.join("../content/Animation/",fileName)        
    writervideo = animation.writers['ffmpeg'](fps=round(1/dTAnim)) 
    anim.save(f, writer=writervideo, dpi=dpi)

    return None
