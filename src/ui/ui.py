class ui:
    def __init__(self, service):
        self._service = service

    def welcome_message(self):
        print("=======================================================")
        print("            -----Welcome to the game!-----             ")
        print("      Today you will play against the computer!        ")
        print("To play the game simply press the number of the column!")
        print("=======================================================")

    def read_move(self):
        try:
            command = input("Enter the column for your next move: ")
            self._service.player_move(command)
        except Exception as ve:
            print(str(ve))

    def display_board(self):
        print(self._service.display_board())

    def start(self):
        self.welcome_message()
        while True:
            self.display_board()
            self.read_move()
            print("\n")
            self.display_board()
            if self._service.check_winner(1) == 1:
                self.display_board()
                print("Congrats! You won the game!")
                break
            if self._service.check_winner(1) == 0:
                self.display_board()
                print("The game is a tie!")
                break
            self._service.computer_move()
            print("\n")
            if self._service.check_winner(1) == -1:
                self.display_board()
                print("You lost! :(")
                break
            if self._service.check_winner(1) == 0:
                self.display_board()
                print("The game is a tie!")
                break