import os
import subprocess

user_selection = input('Enter your Oprtion: ')

def execute_clab_cmd(user_opt):
    # CLAB run command
    cmd_up = 'containerlab deploy -t arista.labtest.yml'
    cmd_down = 'containerlab destroy -t arista.labtest.yml --graceful'
    if user_opt == 1:
        temp = subprocess.Popen([cmd_up], stdout= subprocess.PIPE)
        output = str(temp.communicate())
        return output
    elif user_opt == 2:
        temp = subprocess.Popen([cmd_down], stdout= subprocess.PIPE)
        output = str(temp.communicate())
        return output
    else:
        return 'Error or Invalid option'

print(f'You Selected Option:  {user_selection}')

execute_clab_cmd(user_selection)