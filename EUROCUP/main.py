from CONTROL.manage_DATAS import Manage
from CONTROL.manage_COMMAND import Manage_COMMAND
from FOOTBALL.football import Football


def main():
    exit_command = True
    Manage_COMMAND.head()
    while exit_command:
        command_line = input(">>>> ")
        keyword_list = command_line.split(" ")
        if len(keyword_list) == 1: 
            if command_line.lower() == 'exit':
                exit_command = False
            else:
                Manage_COMMAND.solo_command(command_line)
        elif keyword_list[1].lower() == 'help': Manage_COMMAND.help_command(keyword_list)
        elif keyword_list[0].lower() == 'show': Manage_COMMAND.show_command(keyword_list)
        elif keyword_list[0].lower() == 'makebet': Manage_COMMAND.makebet_command(keyword_list)
        elif keyword_list[0].lower() == 'resultbet': Manage_COMMAND.resultbets_command(keyword_list)
        elif keyword_list[0].lower() == 'hit': Manage_COMMAND.hit_command(keyword_list)
        else:
            if len(keyword_list) == 1:
                print(f"'{keyword_list[0]}' isn't a inner command of this program")
            else:
                print(f"'{keyword_list[0]}' isn't a inner command of this program")
                for keyword in keyword_list[1:]:
                    for stock_command, param in Manage_COMMAND.detail_command.items():
                        if keyword in param.keys():
                            print(f"'{keyword}' isn't a inner command of this program") 


