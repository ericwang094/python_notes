# for x,y,z,n write a permutation that 0-x, 0-y, 0-z but the array of elements not sum to be n
# for example x = 1, y = 1, z = 2
# output [[0,0,0],[0,0,1],[0,0,2],[0,1,0]...[1,1,2]]
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
