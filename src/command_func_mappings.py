# import TYPING

from utils.commands import Commands

COMMAND_OBJ = Commands()


COMMAND_FUNC_MAPPINGS = {
    'touch': COMMAND_OBJ.touch_command,
    'mkdir': COMMAND_OBJ.mkdir_command
}