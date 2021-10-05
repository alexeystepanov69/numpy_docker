# This is a sample Python script.
import numpy as np
from qvd import qvd_reader

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    print(f'Numpy pi = {np.pi}')
    var = 0
    try:
        with open("/tmp/numpy_var.txt", "r") as f:
            var = float(f.readline())
    except BaseException as e:
        print(f"Run Error: {e}")

    with open("/tmp/numpy_docker.txt", 'w') as f:
        f.write(f"Numpy.pi = {np.pi}\n")
        f.write(f"Result = {np.pi + var}")

    print(f"Success! Result = {np.pi + var}")

    df = qvd_reader.read('credit_cards.qvd')
    print(df)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
