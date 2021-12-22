
#---
# Save Figure:
def saveFig(fig,nameFig): 
    # ------- the name must contain the figure format:
    # e.g., nameFig = 'Position.png' or nameFig = 'linearVelocity.eps'

    fig.savefig(nameFig, dpi=300, bbox_inches='tight')