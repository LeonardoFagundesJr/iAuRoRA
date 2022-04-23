
#---
# Save Figure:
def saveFig_old(fig,nameFig): 
    # ------- the name must contain the figure format:
    # e.g., nameFig = 'Position.png' or nameFig = 'linearVelocity.eps'
    import os
    
    nameFig = os.path.join("/content/Figures/",nameFig)
    fig.savefig(nameFig, dpi=300, bbox_inches='tight')

    
#---
# Save Figure:
def saveFig(fig,nameFig): 
    # ------- the name must contain the figure format:
    # e.g., nameFig = 'Position.png' or nameFig = 'linearVelocity.eps'
    import os

    if not(os.path.isdir('../content/Figures/')):
        os.mkdir('../content/Figures/')

    nameFig = os.path.join("../content/Figures/",nameFig)        

    fig.savefig(nameFig, dpi=600, bbox_inches='tight')
