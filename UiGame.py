from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox
from Ui.Mastermind_ui import Ui_MainWindow
from PySide6.QtCore import Slot
from game import generate_code, TRIES, check_code, CODE_LENGTH

class mainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        
        self._triesLeft = 10
        self._code = []
        self._color1 = None
        self._color2 = None
        self._color3 = None
        self._color4 = None
    
        
        self.GameButtom.clicked.connect(self.ButtomClick)
        
        
        self.Guess1.currentIndexChanged.connect(
            lambda a:self.changeCmbColor(a,self.Guess1)
            )
        self.Guess2.currentIndexChanged.connect(
            lambda a:self.changeCmbColor(a,self.Guess2)
            )
        self.Guess3.currentIndexChanged.connect(
            lambda a:self.changeCmbColor(a,self.Guess3)
            )
        self.Guess4.currentIndexChanged.connect(
            lambda a:self.changeCmbColor(a,self.Guess4)
            )
        
        
    def restarGame(self):
        self._triesLeft = 10
        self.GameButtom.setText("Start")
        self.Tries.setText("Clique em Start para começar!")
        self.GameText.setText(u"Bem-vindo ao mastemind, voc\u00ea tem 10 chances de adivinhar o c\u00f3digo!")
        self.configGuesses(False)
        for i in range(4):
            self.findResult(i).setStyleSheet("background-color: black; border-radius:20px;")
            
        
    def changeTries(self):
        self.Tries.setText(f"{self._triesLeft} Tentativas Restantes")
        self._triesLeft -= 1
        
    def appendColors(self):
        colorsList = [self._color1,self._color2,self._color3,self._color4]
        return colorsList
    
        
    
    def findResult(self, i):
        match i:
            case 0: 
                return self.Result1
            case 1: 
                return self.Result2
            case 2: 
                return self.Result3
            case 3: 
                return self.Result4
            case _:
                return self.Result1
        
        
        
    def changeresultFrame(self, guess, color_counts):
        for i in range(4):
            if guess[i] == self._code[i]:
                self.findResult(i).setStyleSheet("background-color: green; border-radius:20px;")
            else:
                self.findResult(i).setStyleSheet("background-color: red;  border-radius:20px;")
                if guess[i] in color_counts and color_counts[guess[i]] > 0:
                    self.findResult(i).setStyleSheet("background-color: orange; border-radius:20px;")
                    color_counts[guess[i]] -= 1


                        
                
    
    def changeCmbColor(self,Index,Cmb:QComboBox):
        match Index:
            case 0:
                backColor = "#FF0000"
                color = "#FFFFFF"
                colorSet = "R"
            case 1:
                backColor = "#FFFFFF"
                color = "black"
                colorSet = "W"
            case 2:
                backColor = "#0059FF"
                color = "black"
                colorSet = "B"
            case 3:
                backColor = "#FFEA00"
                color = "black"
                colorSet = "Y"
            case 4:
                backColor = "#FF6200"
                color = "black"
                colorSet = "O"
            case 5:
                backColor = "#1EFF00"
                color = "black"
                colorSet = "G"
            case _:
                backColor = "black"
                color = "#FFFFFF"
                colorSet = "N"
                
        match Cmb.objectName():
            case "Guess1":
                self._color1 = colorSet
            case "Guess2":
                self._color2 = colorSet
            case "Guess3":
                self._color3 = colorSet
            case "Guess4":
                self._color4 = colorSet

        Cmb.setStyleSheet(f"background-color: {backColor}; color: {color};")
        
    def setFinalScreen(self,win):
        self.GameButtom.setText(u"Recomeçar")
        if win == True:
            self.Tries.setText(f"Você acertou em {10-self._triesLeft} tentativas!!")
        else:
            self.Tries.setText(f"Você perdeu o jogo!")
            
        
    def ButtomClick(self):
        match self.GameButtom.text():
            case "Recomeçar":
                self.restarGame()
            case "Start":
                self._code = generate_code()
                self.GameText.setText(u"Escolha as cores e aperte o botão Guess.")
                self.Tries.setText(f"{self._triesLeft} Tentativas Restantes")
                self.GameButtom.setText(u"Guess")
                self.configGuesses(True)
            case _:
                if self._triesLeft > 0:
                    guess = self.appendColors()
                    correct_pos, color_counts = check_code(guess, self._code)
                    self.changeresultFrame(guess, color_counts)
                    self.changeTries()
                    if correct_pos == CODE_LENGTH:
                        self.setFinalScreen(True)
                else:
                        self.setFinalScreen(False)
        
        
    def configGuesses(self, start):
        self.Guess1.setEnabled(start)
        self.Guess2.setEnabled(start)
        self.Guess3.setEnabled(start)
        self.Guess4.setEnabled(start)
        if start:
            self.Guess1.removeItem(0)
            self.Guess2.removeItem(0)
            self.Guess3.removeItem(0)
            self.Guess4.removeItem(0)
        else:
            self.Guess1.insertItem(0,u"None")
            self.Guess2.insertItem(0,u"None")
            self.Guess3.insertItem(0,u"None")
            self.Guess4.insertItem(0,u"None")

            self.Guess1.setCurrentIndex(0)
            self.Guess2.setCurrentIndex(0)
            self.Guess3.setCurrentIndex(0)
            self.Guess4.setCurrentIndex(0)
            
            self.changeCmbColor(8,self.Guess1)
            self.changeCmbColor(8,self.Guess2)
            self.changeCmbColor(8,self.Guess3)
            self.changeCmbColor(8,self.Guess4)
            
            
    
def startwindow():
    app = QApplication()
    MainWindow = mainWindow()
    MainWindow.show()
    app.exec()
