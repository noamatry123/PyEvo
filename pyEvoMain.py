__author__ = 'user-pc'
import classes
import graphics
import algorithm


def main():
    graphicModule = graphics.pyGraphics()
    algoModule = algorithm.pyAlgorithm()
    running = True
    while running:
        algoModule.nextStep()
        running = graphicModule.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,
                                          [algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
