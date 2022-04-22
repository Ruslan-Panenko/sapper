field = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', 2, 1, 0, '#', '#', '#', '#'],
    ['#', 2, 0, 0, '#', '#', '#', '#'],
    [1, 1, 0, 0, '#', '#', '#', '#'],
    [0, 0, 1, 2, '#', '#', '#', '#'],
    [0, 0, 1, '#', '#', '#', '#', '#'],
]

 # '''
 #   # | # | # | # | # | # | # | # |
 #   # | # | # | # | # | # | # | # |
 #   # | # | # | # | # | # | # | # |
 #   # | 2 | 1 | 0 | # | # | # | # |
 #   # | 2 | 0 | 0 | # | # | # | # |
 #   1 | 1 | 0 | 0 | # | # | # | # |
 #   0 | 0 | 1 | 2 | # | # | # | # |
 #   0 | 0 | 1 | # | # | # | # | # |
 # '''


# '''
#   # | # | # | # | # | # | # | # |
#   # | # | # | # | # | # | # | # |
#   # | # | # | # | # | # | # | # |
#   b | 2 | 1 | 0 | # | # | # | # |
#   b | 2 | 0 | 0 | # | # | # | # |
#   1 | 1 | 0 | 0 | # | # | # | # |
#   0 | 0 | 1 | 2 | # | # | # | # |
#   0 | 0 | 1 | b | # | # | # | # |
# '''

def print_field(field):
    print('\n\n')
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=' | ')
        print()



def main(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] in range(1, 10):
                counter = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if 7 >= i + x >= 0 and 7 >= j + y >= 0:
                            if field[i + x][j + y] == '#':
                                counter += 1

                if counter == field[i][j]:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if 7 >= i + x >= 0 and 7 >= j + y >= 0:
                                if field[i + x][j + y] == '#':
                                    field[i + x][j + y] = 'b'


            print(field[i][j], end=' | ')


        print()

    print_field(field)


if __name__ == '__main__':
    main(field)
