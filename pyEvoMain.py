__author__ = 'user-pc'
import classes
import graphics
def main():
    graphicModule=graphics.pyGraphics()
    running=True
    while running:
        running=graphicModule.drawBoard()
if __name__ == "__main__":
    main()