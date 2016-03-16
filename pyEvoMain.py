__author__ = 'user-pc'
import classes
import graphics
import algorithm

framerate=100
def main():
    screenheight=800
    screenwidth=600
    graphicModule = graphics.pyGraphics(framerate,screenheight,screenwidth)
    algoModule = algorithm.pyAlgorithm(screenwidth,screenheight)
    running = True
    while running:
        algoModule.nextStep()
        running = graphicModule.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,
                                          [algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
