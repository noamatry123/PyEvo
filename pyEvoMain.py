__author__ = 'user-pc'
import classes
import graphics
import algorithm
def main():
    graphicModule=graphics.pyGraphics()
    algoModule=algorithm.pyAlgorithm()
    running=True
    while running:
        algoModule.nextStep()
        running=graphicModule.drawBoard(algoModule.myCell,None,None,None)
if __name__ == "__main__":
    main()