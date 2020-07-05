# Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

# For example, given the following matrix:

# [['F', 'A', 'C', 'I'],
#  ['O', 'B', 'Q', 'P'],
#  ['A', 'N', 'O', 'B'],
#  ['M', 'A', 'S', 'S']]

# and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.

def find_word_in_2d_matrix(matrix, target_word):

    target_word_list = list(target_word)

    while True:
        
        for row in matrix:

            for i in row:
                
                if i == target_word_list[0]:
                    
                    target_word_list.pop(0)
                    
                    if len(target_word_list) == 0:
                        
                        return True

        return False

mat = [['F', 'A', 'C', 'I'], ['O', 'B', 'Q', 'P'], ['A', 'N', 'O', 'B'], ['M', 'A', 'S', 'S']]
word = 'FOAM'
word2 = 'MASS'
word3 = 'CUNT'

print(find_word_in_2d_matrix(mat, word2))