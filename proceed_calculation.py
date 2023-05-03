from tree_object import *
from functions_to_calculate import *

calcul_functions = {"FUNC_+":make_sum, "FUNC_-":make_substraction, "FUNC_*":make_multiplication, "FUNC_/":make_division, "FUNC_POWER":make_power}

def proceed_calculation(calcul_tree):

    """Input : A calcul represented by an output of the build_tree function.
    Output : An integer value which is the result of the calcul."""

    # TODO : Verify what happens where there is no left child and/or right child and the node is a function.

    if type(calcul_tree.getData()) not in [str, type(None)]: # If the value is a number, the function returns the number to be used recursively.
        return calcul_tree.getData()
    else:
        f = calcul_functions[calcul_tree.getData()] # Getting the function to use.
        return f(proceed_calculation(calcul_tree.getLeft()), proceed_calculation(calcul_tree.getRight())) # Proceeding calculation with the left child and the right child. If they are functions, the result will be proceed recursively, else the result will be a number to use directly.



if __name__ == "__main__":
    print(proceed_calculation(BinaryTree("FUNC_+", BinaryTree("FUNC_*", BinaryTree(1), BinaryTree(5)), BinaryTree("FUNC_*", BinaryTree(2), BinaryTree(10)))))
# TODO : Make appropriate tests.