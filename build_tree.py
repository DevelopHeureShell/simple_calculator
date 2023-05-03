import tree_object
from tree_object import *

def build_tree(calcul_tokenise, rank=0):

    operations_priority_order = {
        "FUNC_+" : 1,
        "FUNC_-" : 1,
        "FUNC_*" : 2,
        "FUNC_/" : 2
    }

    """Input : A calcul represented by an output of the tokenization function.
    Output : A tree which represents a calcul with priorities."""

    calcul_tokenise_after_handled_parenthesis = []

    # First of all, the case of parenthesis is handled.

    i = 0
    while i < len(calcul_tokenise):
        if calcul_tokenise[i][0] == "PRIORITY_SIGN":
            if calcul_tokenise[i][1] == "PRIORITY_(":
                nb_open_parenthesis = 1  # Number of parenthesis opened without being closed.
                i2 = i+1
                sub_calcul_tokenise = []  # The elements in the parenthesis, without the parenthesis because they were handled.
                while nb_open_parenthesis > 0:  # While there is parenthesis not closed.
                    if i2 >= len(calcul_tokenise):  # If there is a parenthesis not closed, an error is raised.
                        raise SyntaxError("The parenthesis opened at character " + str(rank+i) + " is not closed.")
                    elif calcul_tokenise[i2][1] == "PRIORITY_(":  # If there are other parenthesis in the initial parenthesis, the number of parenthesis to close is incremented to do not consider the next closed parenthesis as the end of the sub calcul.
                        nb_open_parenthesis += 1
                        sub_calcul_tokenise.append(calcul_tokenise[i2])
                    elif calcul_tokenise[i2][1] == "PRIORITY_)":  # If there is a closed parenthesis, the number of not closed parenthesis is decremented.
                        if nb_open_parenthesis < 1: # If there is a closed parenthesis not linked to an open parenthesis, an error is raised because the calcul can not be true.
                            raise SyntaxError("The parenthesis closed at character " + str(rank+i2) + " has no matching opening parenthesis.")
                        nb_open_parenthesis -= 1
                        if nb_open_parenthesis > 0:  # To do not add a closed parenthesis if it is the end of the sub calcul.
                            sub_calcul_tokenise.append(calcul_tokenise[i2])
                    else:
                        sub_calcul_tokenise.append(calcul_tokenise[i2])
                    i2 += 1
                calcul_tokenise_after_handled_parenthesis.append(build_tree(sub_calcul_tokenise, i2))
                i = i2
            else:
                raise SyntaxError("The parenthesis closed at character " + str(rank+i) + " has no matching opening parenthesis.")
        else:
            calcul_tokenise_after_handled_parenthesis.append(calcul_tokenise[i])
            i += 1

    # The tree is therefore built.

    for number_of_passages in range(1,max(operations_priority_order.values())):
        calcul_tokenise_after_handled_parenthesis = [e for e in calcul_tokenise_after_handled_parenthesis if e is not None] # Deleting Nones.

        i = 0
        final_tree = calcul_tokenise_after_handled_parenthesis[0]
        while i < len(calcul_tokenise_after_handled_parenthesis):

            if type(calcul_tokenise_after_handled_parenthesis[i]) is tuple: # If it is not a BinaryTree or None.

                if calcul_tokenise_after_handled_parenthesis[i][0] == "FUNCTION":
                    if operations_priority_order[calcul_tokenise_after_handled_parenthesis[i][1]] == number_of_passages: # If it's the time to make this calcul.
                        if type(calcul_tokenise_after_handled_parenthesis[i-1]) is not tree_object.BinaryTree:
                            calcul_tokenise_after_handled_parenthesis[i-1] = BinaryTree(calcul_tokenise_after_handled_parenthesis[i-1][1])
                        if type(calcul_tokenise_after_handled_parenthesis[i+1]) is not tree_object.BinaryTree:
                            calcul_tokenise_after_handled_parenthesis[i+1] = BinaryTree(calcul_tokenise_after_handled_parenthesis[i+1][1])
                        calcul_tokenise_after_handled_parenthesis[i+1] = BinaryTree(calcul_tokenise_after_handled_parenthesis[i][1], calcul_tokenise_after_handled_parenthesis[i-1], calcul_tokenise_after_handled_parenthesis[i + 1])
                        calcul_tokenise_after_handled_parenthesis[i-1] = None # The just-before-last element of calcul_tokenise_after_handled_parenthesis was included into the tree, so it is deleted from calcul_tokenise_after_handled_parenthesis.
                        calcul_tokenise_after_handled_parenthesis[i] = None
                        final_tree = calcul_tokenise_after_handled_parenthesis[i+1]
                        i += 2 # The element after the function was already included too, so it is not considered a second time.

                elif calcul_tokenise_after_handled_parenthesis[i][0] == "NUMBER":
                    calcul_tokenise_after_handled_parenthesis[i] = BinaryTree(calcul_tokenise[i][1])
                    i += 1

            else:
                i += 1 # If the element is a Tree, the program go to the next element.

    return final_tree