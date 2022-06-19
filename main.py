from imports import *

filename = 'pictures.py'
while True:
    """However, you should be careful with the '.wait()'"""
    p = subprocess.Popen("python3 "+filename, shell=True).wait()

    """#if your there is an error from running 'my_python_code_A.py',
    the while loop will be repeated,
    otherwise the program will break from the loop"""
    if p != 0:
        continue
    else:
        print('problem - restarting')
        break

time.sleep(1)
print("Running")