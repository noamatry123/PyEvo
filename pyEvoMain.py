__author__ = 'user-pc'
import classes
import graphics
import algorithm


def main():
    framerate=200
    screenwidth=800
    screenheight=600
    graphicModule = graphics.pyGraphics(framerate,screenheight,screenwidth)
    algoModule = algorithm.pyAlgorithm()
    running = True
    while running:
        algoModule.nextStep()
        running = graphicModule.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,
                                          [algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
