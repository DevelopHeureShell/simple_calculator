supported_functions = ['+', '-', '*', '/', '**']

def tokenization(calcul):

    """Input : A calcul represented by a string.
    Output : A token list usuable to build a tree.
    This function supports sum, substractions, multiplications and divisions of integer values.
    Parenthesis are usuable."""

    if not calcul: # If no calcul were given, the function could not run properly.
        raise SyntaxError("No calcul were given.")

    calcul_tokenise = []
    i = 0


    while i<len(calcul):

        if calcul[i] in supported_functions:
            calcul_tokenise.append(("FUNCTION", "FUNC_"+calcul[i]))
            i += 1

        elif calcul[i] in ['(', ')']:
            calcul_tokenise.append(("PRIORITY_SIGN", "PRIORITY_"+calcul[i]))
            i += 1

        elif calcul[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            nombre = str(calcul[i])
            while i+1<len(calcul) and calcul[i+1] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                i += 1
                nombre = nombre + str(calcul[i])
            calcul_tokenise.append(("NUMBER", int(nombre)))
            i += 1

        else:
            raise SyntaxError("At character " + str(i) + " : Invalid symbol.")

    return calcul_tokenise

if __name__ == "__main__":
    print(tokenization("1*2+5"))
    print(tokenization("1*2+5/2*7-2"))
# TODO : Make appropriate tests.