__author__ = 'user-pc'
import classes
import graphics
import algorithm
import easygui
import consts
def main():
    consts.screenwidth=int(easygui.enterbox("Enter width","","800"))
    consts.screenheight=int(easygui.enterbox("Enter height","","600"))

    graphicModule = graphics.pyGraphics(consts.framerate,consts.screenwidth,consts.screenheight)
    algoModule = algorithm.pyAlgorithm(consts.screenwidth,consts.screenheight)
    running = True
    while running:
        algoModule.nextStep()
        running = graphicModule.drawBoard(algoModule.myCell, algoModule.cellList, algoModule.foodList,
                                          [algoModule.myEggs, algoModule.cellEggs])


if __name__ == "__main__":
    main()
