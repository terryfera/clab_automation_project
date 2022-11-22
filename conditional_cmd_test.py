
import subprocess

user_input = input('Enter your option: ')


if not user_input:
    print('Please, select an option')
elif user_input == 1:
    p1 = subprocess.run('containerlab deploy -t arista.labtest.yml', capture_output=True, text=True, shell=True)
elif user_input == 2:
    p2 = subprocess.run('containerlab destroy -t arista.labtest.yml --graceful', capture_output=True, text=True, shell=True)

#print(p1.stdout)
