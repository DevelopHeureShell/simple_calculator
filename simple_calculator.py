### A basic calculator. ###

from tokenization import *
from build_tree import *
from proceed_calculation import proceed_calculation


def prompt(debug):
    if debug is False:
        calcul = input("Enter the calcul, or exit to quit the program : ")
        while calcul not in ["exit", "Exit", "exit()", "Exit()", "\"exit\"", "\"Exit\""]:
            try:
                print(proceed_calculation(build_tree(tokenization(calcul))))
            except Exception as error:
                print(error)
            finally:
                calcul = input("Enter another calcul, or \"exit\" to quit the program : ")
    elif debug is True:
        calcul = input("Enter the calcul, or exit to quit the program : ")
        while calcul not in ["exit", "Exit", "exit()", "Exit()", "\"exit\"", "\"Exit\""]:
                print(proceed_calculation(build_tree(tokenization(calcul))))
                calcul = input("Enter another calcul, or \"exit\" to quit the program : ")

#if __name__ == "__main__":
    #prompt(debug=False)

if __name__ == "__main__":
    prompt(debug=True)

### NOTES : ###

# To add another function to do a calcul, you must define the function in :
# - tokenization.py : add the symbol of the function in the supported_functions list.
# - proceed_calculation.py : add a reference to the function in the calcul_functions list.
# - functions_to_calculate.py : add the function to proceed the calcul.
# - build_tree.py : add in the dictionary operations_priority_order the number of the priority order (1 the lowest).
# Note : You might need to modify build_tree.py if you have specific needs, like a change in priority order.