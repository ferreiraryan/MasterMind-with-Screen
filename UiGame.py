from PySide6.QtWidgets import QMainWindow, QApplication, QComboBox
from PySide6.QtCore import Slot
from Ui.Mastermind_ui import Ui_MainWindow
from game import generate_code, check_code, CODE_LENGTH

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)

        # Initialize game state
        self._tries_left = 10
        self._code = []
        self._current_guess: list[str] = [""] * CODE_LENGTH


        # Connect UI elements
        self.GameButtom.clicked.connect(self.handle_button_click)
        self.Guess1.currentIndexChanged.connect(lambda index: self.update_guess(0, index, self.Guess1))
        self.Guess2.currentIndexChanged.connect(lambda index: self.update_guess(1, index, self.Guess2))
        self.Guess3.currentIndexChanged.connect(lambda index: self.update_guess(2, index, self.Guess3))
        self.Guess4.currentIndexChanged.connect(lambda index: self.update_guess(3, index, self.Guess4))

    def reset_game(self):
        """Reset the game to its initial state."""
        self._tries_left = 10
        self._code = generate_code()
        self._current_guess = [""] * CODE_LENGTH  # Inicialização como lista de strings vazias
        self.update_ui_for_reset()
        self.GameText.setText("Bem-vindo ao Mastermind! Clique em Start para começar.")

    def update_ui_for_reset(self):
        """Reset UI components to their initial states."""
        self.GameButtom.setText("Start")
        self.Tries.setText("Clique em Start para começar!")
        self.set_guess_inputs_enabled(False)
        for i in range(CODE_LENGTH):
            self.find_result_label(i).setStyleSheet("background-color: black; border-radius:20px;")

    def handle_button_click(self):
        """Handle the main button click for starting or guessing."""
        if self.GameButtom.text() == "Recomeçar":
            self.reset_game()
        elif self.GameButtom.text() == "Start":
            self._code = generate_code()
            self.GameButtom.setText("Guess")
            self.Tries.setText(f"{self._tries_left} Tentativas restantes")
            self.set_guess_inputs_enabled(True)
            self.GameText.setText("Escolha as cores e clique em Guess.")
        else:
            self.process_guess()

    def process_guess(self):
        """Process the player's guess and update the UI."""
        if "" in self._current_guess:  # Verifica strings vazias em vez de None
            self.GameText.setText("Por favor, selecione todas as cores antes de continuar.")
            return

        # check_code agora recebe o tipo correto
        correct_pos, color_counts = check_code(self._current_guess, self._code)
        self.update_result_frames(correct_pos, color_counts)
        self._tries_left -= 1
        self.Tries.setText(f"{self._tries_left} Tentativas restantes")

        if correct_pos == CODE_LENGTH:
            self.set_final_screen(True)
        elif self._tries_left == 0:
            self.set_final_screen(False)

    def update_guess(self, index: int, color_index: int, combo_box: QComboBox):
        """Update the guess array and the visual style of the combo box."""
        color_map = {0: "", 1: "R", 2: "W", 3: "B", 4: "Y", 5: "O", 6: "G"}
        style_map = {
            0: ("#000", "#FFFFFF"),
            1: ("#FF0000", "#FFFFFF"),
            2: ("#FFFFFF", "black"),
            3: ("#0059FF", "black"),
            4: ("#FFEA00", "black"),
            5: ("#FF6200", "black"),
            6: ("#1EFF00", "black"),
        }

        if color_index in color_map:
            self._current_guess[index] = color_map[color_index]
            background, color = style_map[color_index]
            combo_box.setStyleSheet(f"background-color: {background}; color: {color};")

    def update_result_frames(self, correct_pos: int, color_counts: dict):
        """Update the result frames based on the guess outcome."""
        for i, color in enumerate(self._current_guess):
            label = self.find_result_label(i)
            if color == self._code[i]:
                label.setStyleSheet("background-color: green; border-radius:20px;")
            elif color_counts.get(color, 0) > 0:
                label.setStyleSheet("background-color: orange; border-radius:20px;")
                color_counts[color] -= 1
            else:
                label.setStyleSheet("background-color: red; border-radius:20px;")

    def set_guess_inputs_enabled(self, enabled: bool):
        """Enable or disable the guess input combo boxes."""
        for combo_box in [self.Guess1, self.Guess2, self.Guess3, self.Guess4]:
            combo_box.setEnabled(enabled)

    def find_result_label(self, index: int):
        """Find the result label widget based on the index."""
        return [self.Result1, self.Result2, self.Result3, self.Result4][index]

    def set_final_screen(self, win: bool):
        """Set the final game state on the UI."""
        self.GameButtom.setText("Recomeçar")
        if win:
            self.Tries.setText(f"Você acertou em {10 - self._tries_left} tentativas!")
        else:
            self.Tries.setText(f"Você perdeu! O código era: {' '.join(self._code)}")

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
