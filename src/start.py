from src.ui.ui import ui
from src.command_validator import CommandValidator
from src.repository.repository import RepoGame
from src.service.service import ServiceGame
validator = CommandValidator()
repo = RepoGame()
service = ServiceGame(repo, validator)
ui = ui(service)
ui.start()