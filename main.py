import re


#script for 
#https://minesweeper.online/ru/
#1) start game
#2) find div with id #A43
#3) copy it and past to "source_text" variable
#4) Change width and heigth in get_field() on your  sizes
#5) Run
#6) click on cell with 'c' tag




source_text = '''

<div id="A43" class="pull-left"><div id="cell_0_0" class="cell size40 hd_closed" data-x="0" data-y="0"></div><div id="cell_1_0" class="cell size40 hd_closed" data-x="1" data-y="0"></div><div id="cell_2_0" class="cell size40 hd_closed" data-x="2" data-y="0"></div><div id="cell_3_0" class="cell size40 hd_closed" data-x="3" data-y="0"></div><div id="cell_4_0" class="cell size40 hd_closed" data-x="4" data-y="0"></div><div id="cell_5_0" class="cell size40 hd_closed" data-x="5" data-y="0"></div><div id="cell_6_0" class="cell size40 hd_closed" data-x="6" data-y="0"></div><div id="cell_7_0" class="cell size40 hd_closed" data-x="7" data-y="0"></div><div id="cell_8_0" class="cell size40 hd_closed" data-x="8" data-y="0"></div><div id="cell_9_0" class="cell size40 hd_closed" data-x="9" data-y="0"></div><div class="clear"></div><div id="cell_0_1" class="cell size40 hd_closed" data-x="0" data-y="1"></div><div id="cell_1_1" class="cell size40 hd_closed" data-x="1" data-y="1"></div><div id="cell_2_1" class="cell size40 hd_closed" data-x="2" data-y="1"></div><div id="cell_3_1" class="cell size40 hd_closed" data-x="3" data-y="1"></div><div id="cell_4_1" class="cell size40 hd_closed hd_flag" data-x="4" data-y="1"></div><div id="cell_5_1" class="cell size40 hd_opened hd_type3" data-x="5" data-y="1"></div><div id="cell_6_1" class="cell size40 hd_opened hd_type1" data-x="6" data-y="1"></div><div id="cell_7_1" class="cell size40 hd_opened hd_type2" data-x="7" data-y="1"></div><div id="cell_8_1" class="cell size40 hd_opened hd_type3" data-x="8" data-y="1"></div><div id="cell_9_1" class="cell size40 hd_opened hd_type2" data-x="9" data-y="1"></div><div class="clear"></div><div id="cell_0_2" class="cell size40 hd_closed" data-x="0" data-y="2"></div><div id="cell_1_2" class="cell size40 hd_opened hd_type2" data-x="1" data-y="2"></div><div id="cell_2_2" class="cell size40 hd_opened hd_type1" data-x="2" data-y="2"></div><div id="cell_3_2" class="cell size40 hd_opened hd_type3" data-x="3" data-y="2"></div><div id="cell_4_2" class="cell size40 hd_closed hd_flag" data-x="4" data-y="2"></div><div id="cell_5_2" class="cell size40 hd_opened hd_type2" data-x="5" data-y="2"></div><div id="cell_6_2" class="cell size40 hd_opened hd_type0" data-x="6" data-y="2"></div><div id="cell_7_2" class="cell size40 hd_opened hd_type0" data-x="7" data-y="2"></div><div id="cell_8_2" class="cell size40 hd_opened hd_type2" data-x="8" data-y="2"></div><div id="cell_9_2" class="cell size40 hd_closed hd_flag" data-x="9" data-y="2"></div><div class="clear"></div><div id="cell_0_3" class="cell size40 hd_closed" data-x="0" data-y="3"></div><div id="cell_1_3" class="cell size40 hd_opened hd_type2" data-x="1" data-y="3"></div><div id="cell_2_3" class="cell size40 hd_opened hd_type0" data-x="2" data-y="3"></div><div id="cell_3_3" class="cell size40 hd_opened hd_type1" data-x="3" data-y="3"></div><div id="cell_4_3" class="cell size40 hd_opened hd_type1" data-x="4" data-y="3"></div><div id="cell_5_3" class="cell size40 hd_opened hd_type1" data-x="5" data-y="3"></div><div id="cell_6_3" class="cell size40 hd_opened hd_type0" data-x="6" data-y="3"></div><div id="cell_7_3" class="cell size40 hd_opened hd_type0" data-x="7" data-y="3"></div><div id="cell_8_3" class="cell size40 hd_opened hd_type2" data-x="8" data-y="3"></div><div id="cell_9_3" class="cell size40 hd_closed hd_flag" data-x="9" data-y="3"></div><div class="clear"></div><div id="cell_0_4" class="cell size40 hd_closed" data-x="0" data-y="4"></div><div id="cell_1_4" class="cell size40 hd_opened hd_type1" data-x="1" data-y="4"></div><div id="cell_2_4" class="cell size40 hd_opened hd_type0" data-x="2" data-y="4"></div><div id="cell_3_4" class="cell size40 hd_opened hd_type0" data-x="3" data-y="4"></div><div id="cell_4_4" class="cell size40 hd_opened hd_type0" data-x="4" data-y="4"></div><div id="cell_5_4" class="cell size40 hd_opened hd_type0" data-x="5" data-y="4"></div><div id="cell_6_4" class="cell size40 hd_opened hd_type0" data-x="6" data-y="4"></div><div id="cell_7_4" class="cell size40 hd_opened hd_type0" data-x="7" data-y="4"></div><div id="cell_8_4" class="cell size40 hd_opened hd_type2" data-x="8" data-y="4"></div><div id="cell_9_4" class="cell size40 hd_opened hd_type2" data-x="9" data-y="4"></div><div class="clear"></div><div id="cell_0_5" class="cell size40 hd_closed" data-x="0" data-y="5"></div><div id="cell_1_5" class="cell size40 hd_opened hd_type1" data-x="1" data-y="5"></div><div id="cell_2_5" class="cell size40 hd_opened hd_type0" data-x="2" data-y="5"></div><div id="cell_3_5" class="cell size40 hd_opened hd_type0" data-x="3" data-y="5"></div><div id="cell_4_5" class="cell size40 hd_opened hd_type0" data-x="4" data-y="5"></div><div id="cell_5_5" class="cell size40 hd_opened hd_type0" data-x="5" data-y="5"></div><div id="cell_6_5" class="cell size40 hd_opened hd_type1" data-x="6" data-y="5"></div><div id="cell_7_5" class="cell size40 hd_opened hd_type1" data-x="7" data-y="5"></div><div id="cell_8_5" class="cell size40 hd_opened hd_type2" data-x="8" data-y="5"></div><div id="cell_9_5" class="cell size40 hd_closed hd_flag" data-x="9" data-y="5"></div><div class="clear"></div><div id="cell_0_6" class="cell size40 hd_closed" data-x="0" data-y="6"></div><div id="cell_1_6" class="cell size40 hd_opened hd_type1" data-x="1" data-y="6"></div><div id="cell_2_6" class="cell size40 hd_opened hd_type0" data-x="2" data-y="6"></div><div id="cell_3_6" class="cell size40 hd_opened hd_type0" data-x="3" data-y="6"></div><div id="cell_4_6" class="cell size40 hd_opened hd_type1" data-x="4" data-y="6"></div><div id="cell_5_6" class="cell size40 hd_opened hd_type1" data-x="5" data-y="6"></div><div id="cell_6_6" class="cell size40 hd_opened hd_type3" data-x="6" data-y="6"></div><div id="cell_7_6" class="cell size40 hd_closed hd_flag" data-x="7" data-y="6"></div><div id="cell_8_6" class="cell size40 hd_opened hd_type3" data-x="8" data-y="6"></div><div id="cell_9_6" class="cell size40 hd_opened hd_type1" data-x="9" data-y="6"></div><div class="clear"></div><div id="cell_0_7" class="cell size40 hd_closed" data-x="0" data-y="7"></div><div id="cell_1_7" class="cell size40 hd_opened hd_type3" data-x="1" data-y="7"></div><div id="cell_2_7" class="cell size40 hd_opened hd_type1" data-x="2" data-y="7"></div><div id="cell_3_7" class="cell size40 hd_opened hd_type0" data-x="3" data-y="7"></div><div id="cell_4_7" class="cell size40 hd_opened hd_type1" data-x="4" data-y="7"></div><div id="cell_5_7" class="cell size40 hd_closed hd_flag" data-x="5" data-y="7"></div><div id="cell_6_7" class="cell size40 hd_opened hd_type3" data-x="6" data-y="7"></div><div id="cell_7_7" class="cell size40 hd_closed hd_flag" data-x="7" data-y="7"></div><div id="cell_8_7" class="cell size40 hd_opened hd_type2" data-x="8" data-y="7"></div><div id="cell_9_7" class="cell size40 hd_opened hd_type0" data-x="9" data-y="7"></div><div class="clear"></div><div id="cell_0_8" class="cell size40 hd_closed" data-x="0" data-y="8"></div><div id="cell_1_8" class="cell size40 hd_closed hd_flag" data-x="1" data-y="8"></div><div id="cell_2_8" class="cell size40 hd_opened hd_type2" data-x="2" data-y="8"></div><div id="cell_3_8" class="cell size40 hd_opened hd_type2" data-x="3" data-y="8"></div><div id="cell_4_8" class="cell size40 hd_opened hd_type3" data-x="4" data-y="8"></div><div id="cell_5_8" class="cell size40 hd_opened hd_type2" data-x="5" data-y="8"></div><div id="cell_6_8" class="cell size40 hd_opened hd_type2" data-x="6" data-y="8"></div><div id="cell_7_8" class="cell size40 hd_opened hd_type1" data-x="7" data-y="8"></div><div id="cell_8_8" class="cell size40 hd_opened hd_type2" data-x="8" data-y="8"></div><div id="cell_9_8" class="cell size40 hd_opened hd_type1" data-x="9" data-y="8"></div><div class="clear"></div><div id="cell_0_9" class="cell size40 hd_closed" data-x="0" data-y="9"></div><div id="cell_1_9" class="cell size40 hd_opened hd_type2" data-x="1" data-y="9"></div><div id="cell_2_9" class="cell size40 hd_opened hd_type2" data-x="2" data-y="9"></div><div id="cell_3_9" class="cell size40 hd_closed hd_flag" data-x="3" data-y="9"></div><div id="cell_4_9" class="cell size40 hd_closed hd_flag" data-x="4" data-y="9"></div><div id="cell_5_9" class="cell size40 hd_opened hd_type1" data-x="5" data-y="9"></div><div id="cell_6_9" class="cell size40 hd_opened hd_type0" data-x="6" data-y="9"></div><div id="cell_7_9" class="cell size40 hd_opened hd_type0" data-x="7" data-y="9"></div><div id="cell_8_9" class="cell size40 hd_opened hd_type1" data-x="8" data-y="9"></div><div id="cell_9_9" class="cell size40 hd_closed hd_flag" data-x="9" data-y="9"></div><div class="clear"></div></div>


'''



text = source_text[70:]


def get_field(text):
    '''
    conwert HTML to list of lists
                                '''
    width = 10
    heigth = 10
    result = []
    arr = text.split('cell ')
    counter = 0
    for _ in range(width):
        res = []
        for _ in range(heigth):

            if 'hd_closed' in arr[counter]:
                res.append('#')
            elif 'hd_type' in arr[counter]:
                el = re.findall('hd_type[0-9]', arr[counter])
                res.append(int(str(el)[9]))
            counter += 1
        result.append(res)
    return result


def print_field(field):
    '''
    print list of lists as matrix
                                '''
    print('\n\n')
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], end=' | ')
        print()


def find_bomb(field):
    '''
    finding where  is boomb
                            '''
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] in range(1, 10):
                counter = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if heigth-1 >= i + x >= 0 and width-1 >= j + y >= 0:
                            if '#' in str(field[i + x][j + y]):
                                counter += 1

                if counter == field[i][j]:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if heigth-1 >= i + x >= 0 and width-1 >= j + y >= 0:
                                if field[i + x][j + y] == '#':
                                    field[i + x][j + y] += 'b'


def open_cell(field):
    '''
    marks cell without boombs
                            '''
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] in range(1, 10):
                counter = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if heigth-1 >= i + x >= 0 and width-1 >= j + y >= 0:
                            if 'b' in str(field[i + x][j + y]):
                                counter += 1
                if counter == field[i][j]:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if heigth-1 >= i + x >= 0 and width-1 >= j + y >= 0:
                                if field[i + x][j + y] == '#':
                                    field[i + x][j + y] = 'c'


field = get_field(text)


width = len(field[0])
heigth = len(field)


def main(field):
    print_field(field)
    find_bomb(field)
    open_cell(field)
    print_field(field)


if __name__ == '__main__':
    main(field)
