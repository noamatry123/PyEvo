__author__ = 'user-pc'
import classes
screenwidth=2
screenheight=2
framerate=30
text=""
askingQuestion=True
counter=0
season=0
godmode=False
mouse_control=True
loadedGame=False
timeUntilPhase2=15
p2radius=999
p2active=False
recording=True
draw_debugging_options=True
sandbox=False
def bigger(x,y):
    if x>=y:
        return x
    else:
        return y

class Location1:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
class Center:
    location=Location1(screenwidth/2,screenheight/2)
center=Center
