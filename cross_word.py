import numpy as np

words_found = []
words_to_find = ['holiday', 'crunchy', 'bows', 'gifts','squares', 'sweet', 'wrapping', 'yummy', 'lights']


def create_puzzle():

    puzzle = np.array([['f','w','l','e','d','s','h','x','z','f','q','v'],['y','x','r','s','d','s','w','e','e','t','g','n'],
     ['c','u','d','a','v','f','l','q','t','l','k','p'], ['q','g','m','x','p','l','i','g','h','t','s','y'],
     ['z','c','j','m','e','p','g','b','l','e','b','h'], ['r','u','c','s','y','w','i','o','n','z','u','o'],
     ['b','c','r','y','q','x','h','n','g','g','n','l'], ['b','s','u','x','q','u','i','e','g','i','o','i'],
     ['g','e','n','r','q','i','a','x','r','f','t','d'], ['c','t','c','l','x','p','a','r','k','t','o','a'],
     ['v','m','h','r','t','j','z','z','e','s','w','y'], ['a','s','y','u','r','b','o','w','s','s','a','y']])

    return puzzle

def solve_puzzle():
    # solve the cross word puzzle

    puzzle = create_puzzle()
    print("Puzzle to solve: \n {}\n".format(puzzle))
    # flip the array to make it easy to take reverse diagonals
    inv_puzzle = np.fliplr(puzzle)

    check_diagonals(puzzle, inv_puzzle)
    check_rows(puzzle)
    check_vertical(puzzle)

    return words_found, puzzle


def check_diagonals(puzzle, inv_puzzle):

    for i in range(len(puzzle)):
        if i == 0:
            diag = np.diag(puzzle, i)
            inv_diag = np.diag(inv_puzzle, i)
            word = ''.join(diag)
            inv_word = ''.join(inv_diag)
            start, stop = find_word(word)
            begin, end = find_word(inv_word)

        else:
            diag1 = np.diag(puzzle, i)
            word1 = ''.join(diag1)
            s1, e1 = find_word(word1)
            diag2 = np.diag(puzzle, -i)
            word2 = ''.join(diag2)
            s2, e2 = find_word(word2)

            # get the reversed puzzle diagonals
            inv_diag1 = np.diag(inv_puzzle, i)
            inv_word1 = ''.join(inv_diag1)
            s_inv, e_inv = find_word(inv_word1)
            inv_diag2 = np.diag(inv_puzzle, -i)
            inv_word2 = ''.join(inv_diag2)
            s_inv2, e_inv2 = find_word(inv_word2)

def check_rows(puzzle):
    for i in range(len(puzzle)):
        word = ''.join(puzzle[i])
        index, stop = find_word(word)
        if index is not None:
            for j in range(index, stop):
                puzzle[i,j] = puzzle[i,j].upper()

def check_vertical(puzzle):
    for i in range(len(puzzle)):
        word = ''.join(puzzle[:,i])
        index, stop = find_word(word)
        if index is not None:
            for j in range(index, stop):
                puzzle[j,i] = puzzle[j,i].upper()

def find_word(word):
    # find the word in the given string
    for w in words_to_find:
        if w in word.lower():
            # find the start index of the word
            index = word.find(w)
            stop = index + len(w)
            words_found.append(w)
            return index, stop
    # if you make it through for loop then its not found
    return None, None



if __name__ == "__main__":
    words, puzzle = solve_puzzle()

    if len(words) == len(words_to_find):
        if sorted(words_to_find) == sorted(words):
            print("You have found all the words! \n {}\n".format(words))
            print(puzzle)
        else:
            print("You did not find all the words\n")
            print(words_found)

    else:
        print("You are missing words\n")
        print(words_found)
