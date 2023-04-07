# Spring 2023 CPSC 335 - Algorithm Engineering 
# Algorithm 1: Exhaustive Search
# Team Members: Priyanka Lee, Danny Garcia, and Gian Carlo Santos 

#!/usr/bin/env python3

def soccer_exhaustive(G):
    # use len function to calculate num of rows and columns
    r = len(G)
    c = len(G[0])
    # calculate length of candidate list 
    length = 𝑟 + 𝑐 - 2
    # initialize counter to 0
    counter = 0
    # iterate through bits in length
    for bits in range(2**length):
        candidate = []
        for k in range(length):
            bit = (bits >> 𝑘) & 1
            if bit == 1:
                candidate.append((0,1)) # appends a right move
            else:
                candidate.append((1,0)) # appends a left move 
        i, j = 0,0
        valid = True
        # iterate over list of moves and check if valid 
        for row_shift, col_shift in candidate:
            i += row_shift
            j += col_shift
            if i >= r or j >= c or G[i][j] == 'X':
                valid = False
                break
            if valid and i == r-1 and j == c-1:
                counter += 1
    return counter

# main function prints output from soccer_exhaustive function
def main():
    r = int(input("Enter the number of rows: "))
    c = int(input("Enter the number of columns: "))
    G = []
    for i in range(r):
        row = input(f"Enter row {i+1} (with 'O' for passable and 'X' for impassable): ")
        G.append(list(row))
    
    print(soccer_exhaustive(G))

if __name__ == "__main__":
    main()

