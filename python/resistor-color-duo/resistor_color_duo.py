COLORS = ['Black','Brown','Red','Orange','Yellow','Green','Blue','Violet','Grey','White']
def value(colors):
    colors = [color.capitalize() for color in colors]
    return COLORS.index(colors[0])*10 + COLORS.index(colors[1])
     
    
