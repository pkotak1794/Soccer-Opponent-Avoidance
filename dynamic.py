def soccer_dyn_prog(F):
    #initialize rows/column
    r = len(F)
    c = len(F[0])
    #the corner case
    if F[0][0] == 'X':
        return 0
    #new matrix
    A = [0][0]
    #general case
    A[0][0] = 1
    for i in range(0, r - 1):
        for j in range(0,c - 1):
            if F[i][j] == 'X':
                A[i][j] = 0
                continue
            above = left = 0
            if i > 0 and F[i-1][j] == 'O' :
                above = A[i-1][j]
            if j > 0 and F[i][j-1] == 'O' :
                left = A[i][j-1]
            A[i][j] += above + left
    return A[r-1][c-1]

def main():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    F = []
    for i in range(r):
        row = input(f"Enter row {i+1} (with 'O' for passable and 'X' for impassable): ")
        F.append(list(row))
    
    print(soccer_dyn_prog(F))
    
if __name__ == "__main__":
    main()
