class CommandValidator:
    def validate_command(self, command):
        errors = []
        user_command = command
        if user_command.isdigit() == False:
            errors.append("The command can't be empty! Please enter a column to play the game")
        if(int(user_command) < 1 or int(user_command) > 7):
            errors.append("Invalid move! Please enter a digit between 1 and 7! ")
        if len(errors) > 0:
            errors_string = '\n'.join(errors)
            raise ValueError(errors_string)
