
def findDisappearedNumbers(nums):
    data = {k: [] for k in range(1, len(nums) + 1)}
    for n in nums:
        if n in data.keys():
            del data[n]
    return list(data.keys())


#print(findDisappearedNumbers([1,1]))

def findWords(words):
       row1 = list("qwertyuiop")
       row2 = list("asdfghjkl")
       row3 = list("zxcvbnm")
       output = []
       for w in words:
           wl = w.lower()

           if wl[0] in row1:
               r = row1
           elif wl[0] in row2:
               r = row2
           elif wl[0] in row3:
               r = row3
           else:
               continue

           is_ok = True
           for c in wl:
               if c not in r:
                   is_ok = False
                   break

           if is_ok:
                output.append(w)

       return output


words = ["Hello","Alaska","Dad","Peace"]
words = ["omk"]
words = ["adsdf","sfd"]
# print(findWords(words))

def transpose(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    tr = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == 0:
                tr.append([])
            tr[j].append(matrix[i][j])
    return tr

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3],[4,5,6]]
# print(transpose(matrix))

def matrixReshape(mat, r, c):
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    rm = len(mat)
    cm = len(mat[0])
    if cm * rm != r*c:
        return mat

    ret = [[]]
    m = 0
    n = 0
    for i in range(rm):
        for j in range(cm):
            ret[-1].append( mat[i][j])
            n += 1
            if n == c:
                n = 0
                m +=1
                if m != r:
                    ret.append([])

    return ret


mat = [[1,2],[3,4]]
r = 1
c = 4
# print( matrixReshape(mat, r, c))


def countBattleships( board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "X":
                count += 1
                if i != len(board) - 1:
                    if board[i+1][j] == "X":
                        count -= 1
                        j += 1
                    elif j != len(board[i])- 1 and board[i][j+1] == "X":
                        count -=1
    return count




board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# print(countBattleships(board))