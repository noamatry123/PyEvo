__author__ = 'user-pc'
import classes
import graphics
import algorithm

framerate=200
def main():
    screenwidth=600
    screenheight=800
    graphicModule = graphics.pyGraphics(framerate,screenheight,screenwidth)
    algoModule = algorithm.pyAlgorithm()
    running = True
    while running:
        algoModule.nextStep()
        running = graphicModule.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,
                                          [algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
