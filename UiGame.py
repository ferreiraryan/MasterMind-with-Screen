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
        
    def changeTries(self):
        self.Tries.setText(f"{self._triesLeft}Tentativas Restantes")
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
        
        
        
    def changeresultFrame(self, guess):
        color_counts = {}
        for color in self._code:
            if color not in color_counts:
                color_counts[color] = 0
            color_counts[color] += 1
            
        for i in range(4):
            if guess[i] == self._code[i]:
                self.findResult(i).setStyleSheet("background-color: green;")
            else:
                self.findResult(i).setStyleSheet("background-color: red;")
            
                if guess[i] in color_counts and color_counts[guess[i]] > 0:
                    self.findResult(i).setStyleSheet("background-color: orange;")
                    color_counts[guess[i]] -= 1


        # for color in self._code:
        #     if color not in color_counts:
        #         color_counts[color] = 0
        #     color_counts[color] += 1

            
        # for guess_color, real_color in zip(guess, self._code):
        #     if guess_color in color_counts and color_counts[guess_color] > 0:
        #         incorrect_pos += 1
        #         color_counts[guess_color] -= 1
                

                        
                
    
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
        
        
    def ButtomClick(self):
        if self.GameButtom.text() == "Start":
            self._code = generate_code()
            self.GameText.setText(u"Escolha as cores e aperte o botão Guess.")
            self.GameButtom.setText(u"Guess")
            self.configGuesses()
            self.changeTries()
            # print(type(self._code))
            
        else:
            self.changeTries()
            # print(type(self.appendColors()))
            guess = self.appendColors()
            correct_pos, incorrect_pos = check_code(guess, self._code)
            
            if correct_pos == CODE_LENGTH:
                print(f"You guessed the code in {11-TRIES} tries!")
                self.changeresultFrame(guess)
            else:
                self.changeresultFrame(guess)

        
        
    def configGuesses(self):
        self.Guess1.setEnabled(True)
        self.Guess2.setEnabled(True)
        self.Guess3.setEnabled(True)
        self.Guess4.setEnabled(True)
        
        self.Guess1.removeItem(0)
        self.Guess2.removeItem(0)
        self.Guess3.removeItem(0)
        self.Guess4.removeItem(0)
        
        
        
        
    
def startwindow():
    app = QApplication()
    MainWindow = mainWindow()
    MainWindow.show()
    app.exec()
