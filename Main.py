
# return img, nested list
def read_ppm_file(f):
    fp = open(f)
    fp.readline()  # reads P3 (assume it is P3 file)
    lst = fp.read().split()
    n = 0
    n_cols = int(lst[n])
    n += 1
    n_rows = int(lst[n])
    n += 1
    max_color_value = int(lst[n])
    n += 1
    img = []
    for r in range(n_rows):
        img_row = []
        for c in range(n_cols):
            pixel_col = []
            for i in range(3):
                pixel_col.append(int(lst[n]))
                n += 1
            img_row.append(pixel_col)
        img.append(img_row)
    fp.close()
    return img, max_color_value


# Works
def img_printer(img):
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                print(img[i][j][k], end=" ")
            print("\t|", end=" ")
        print()


filename = input()
operation = int(input())


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

img=(read_ppm_file(filename)[0])
print(img_printer(img))
# img is 3d list of rgb values
if operation == 1:
    newmin = int(input())
    newmax = int(input())
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            for k in range(cha):
                newval = (img[i][j][k] - 0) / (read_ppm_file(filename)[1] - 0) * (newmax - newmin) + newmin
                # newval is new value for each rgb values
                g = round(newval, 4)
                # g is rounded new value
                img[i][j].pop(k)
                # this deletes old value
                img[i][j].insert(k, g)
                # this adds rounded new value
    img_printer(img)

if operation == 2:
    summ=0
    summ2 = 0
    summ3 = 0
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            summ += img[i][j][0]
            summ2 += img[i][j][1]
            summ3 += img[i][j][2]
    mean1 = summ / (row*col)
    mean2 = summ2 / (row*col)
    mean3 = summ3 / (row*col)
    # these are means for red, green, and blue values
    tot=0
    tot2=0
    tot3=0
    for i in range(row):
        for j in range(col):
            a1 = (img[i][j][0]-mean1)**2
            a2 = (img[i][j][1] - mean2) ** 2
            a3 = (img[i][j][2] - mean3) ** 2
            tot += a1
            tot2 += a2
            tot3 += a3
    standart_dev1 = (tot/(row*col))**(1/2) +1e-6
    standart_dev2 = (tot2 / (row * col)) ** (1 / 2) +1e-6
    standart_dev3 = (tot3 / (row * col)) ** (1 / 2) +1e-6
    # these are standart deviations for red, green, and blue values
    for i in range(row):
        for j in range(col):
            a = (img[i][j][0] - mean1) / standart_dev1
            b = (img[i][j][1] - mean2) / standart_dev2
            c = (img[i][j][2] - mean3) / standart_dev3
            # here it assigns new values
            d = round(a,4)
            e = round(b, 4)
            f = round(c, 4)
            # here it rounds new values
            img[i][j].pop(0)
            img[i][j].insert(0, d)
            img[i][j].pop(1)
            img[i][j].insert(1, e)
            img[i][j].pop(2)
            img[i][j].insert(2, f)
            # here it deletes old values and add new rounded values
    img_printer(img)

if operation == 3:
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    for i in range(row):
        for j in range(col):
            average = (img[i][j][0] + img[i][j][1] + img[i][j][2])/3
            # average is average of rgb values of each pixel
            img[i][j].pop(0)
            img[i][j].insert(0, int(average))
            img[i][j].pop(1)
            img[i][j].insert(1, int(average))
            img[i][j].pop(2)
            img[i][j].insert(2, int(average))
            #here it deletes old values and adds new average values
    img_printer(img)

# I could not write 4 and 5

if operation == 6:
    rangee = int(input())
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    def func(x,y):
        if x == row-1 and y == row-1:
        # if row and colon is odd it ends right bottom corner
            return img
        if x + 1 == row:
        # if colon ends because we cannot go down, we go right
            if -1*rangee < img[x][y][0] - img[x][y + 1][0] < rangee:
                if -1*rangee < img[x][y][1] - img[x][y + 1][1] < rangee:
                    if -1*rangee < img[x][y][2] - img[x][y + 1][2] < rangee:
                    # comparing difference between values and range
                        img[x][y + 1].pop(0)
                        img[x][y + 1].insert(0, img[x][y][0])
                        img[x][y + 1].pop(1)
                        img[x][y + 1].insert(1, img[x][y][1])
                        img[x][y + 1].pop(2)
                        img[x][y + 1].insert(2, img[x][y][2])
                    # assigning if difference between values in range
            return func2(x, y+1)
            # this takes right in the row
        if -1*rangee < img[x][y][0] - img[x+1][y][0] < rangee:
            if -1*rangee < img[x][y][1] - img[x+1][y][1] < rangee:
                if -1*rangee < img[x][y][2] - img[x + 1][y][2] < rangee:
                    # comparing difference between values and range
                    img[x + 1][y].pop(0)
                    img[x + 1][y].insert(0, img[x][y][0])
                    img[x + 1][y].pop(1)
                    img[x + 1][y].insert(1, img[x][y][1])
                    img[x + 1][y].pop(2)
                    img[x + 1][y].insert(2, img[x][y][2])
                    # assigning if difference between values in range
        return func(x+1, y)
        # this takes down in the colon
    def func2(x,y):
        if x == 0 and y == row-1:
        # if row and colon is odd it ends right top corner
            return img
        if x == 0:
        # if we reach top in the colon we go right
            if -1*rangee < img[x][y][0] - img[x][y+1][0] < rangee:
                if -1*rangee < img[x][y][1] - img[x][y+1][1] < rangee:
                    if -1*rangee < img[x][y][2] - img[x][y+1][2] < rangee:
                        # comparing difference between values and range
                        img[x][y + 1].pop(0)
                        img[x][y + 1].insert(0, img[x][y][0])
                        img[x][y + 1].pop(1)
                        img[x][y + 1].insert(1, img[x][y][1])
                        img[x][y+1].pop(2)
                        img[x][y+1].insert(2, img[x][y][2])
                        # assigning if difference between values in range
            return func(x,y+1)
            # this takes right in the row
        if -1*rangee < img[x][y][0] - img[x - 1][y][0] < rangee:
            if -1*rangee < img[x][y][1] - img[x - 1][y][1] < rangee:
                if -1*rangee < img[x][y][2] - img[x - 1][y][2] < rangee:
                    # comparing difference between values and range
                    img[x - 1][y].pop(0)
                    img[x - 1][y].insert(0, img[x][y][0])
                    img[x - 1][y].pop(1)
                    img[x - 1][y].insert(1, img[x][y][1])
                    img[x - 1][y].pop(2)
                    img[x - 1][y].insert(2, img[x][y][2])
                    # assigning if difference between values in range
        return func2(x-1,y)
        # this takes up in the colon
    img_printer(func(0,0))

if operation == 7:
# it is different version of 6th
    rangee = int(input())
    row = len(img)
    col = len(img[0])
    cha = len(img[0][0])
    def func(x,y,z):
        if z == cha-1 and x == row - 1 and y == row-1:
        # if row and colon is odd it ends right bottom corner
            return img
        if x + 1 == row:
            if -1*rangee < img[x][y][z] - img[x][y + 1][z] < rangee:
                img[x][y + 1].pop(z)
                img[x][y + 1].insert(z, img[x][y][z])
            # here we go right because it reached bottom of colon
            return func2(x, y+1, z)
        if -1*rangee < img[x][y][z] - img[x+1][y][z] < rangee:
            img[x + 1][y].pop(z)
            img[x + 1][y].insert(z, img[x][y][z])
            # firstly compares only red values until red values are done
        return func(x+1, y, z)

    def func2(x, y, z):
        if z == cha-1 and x == 0 and y == row-1:
        # if row and colon is even it ends right top corner
            return img
        if x == 0 and y == row-1:
            if -1*rangee < img[x][y][z] - img[x][y][z+1] < rangee:
                img[x][y].pop(z+1)
                img[x][y].insert(z+1, img[x][y][z])
            # if we complete red values, here it passes green values
            return func3(x, y, z + 1)
        if x == 0 and y != row-1:
            if -1*rangee < img[x][y][z] - img[x][y+1][z] < rangee:
                img[x][y + 1].pop(z)
                img[x][y + 1].insert(z, img[x][y][z])
            # here it goes right because we reached top of the colon
            return func(x,y+1,z)
        if -1*rangee < img[x][y][z] - img[x - 1][y][z] < rangee:
            img[x - 1][y].pop(z)
            img[x - 1][y].insert(z, img[x][y][z])
            # it goes top from the bottom
        return func2(x-1,y,z)

    def func3(x,y,z):
        if z == cha-1 and x == 0 and y == row-1:
        # this if probably is not necessary but I wanted to keep it to avoid any error
            return img
        if x + 1 == row:
            if -1*rangee < img[x][y][z] - img[x][y - 1][z] < rangee:
                img[x][y - 1].pop(z)
                img[x][y - 1].insert(z, img[x][y][z])
            # we passed to blue values now we have to go backwards, to the left
            return func4(x, y-1, z)
        if -1*rangee < img[x][y][z] - img[x+1][y][z] < rangee:
            img[x + 1][y].pop(z)
            img[x + 1][y].insert(z, img[x][y][z])
            # backward again, from top to the bottom
        return func3(x+1, y, z)

    def func4(x, y, z):
        if z == cha-1 and x == 0 and y == row-1:
        # this if probably is not necessary but I wanted to keep it to avoid any error
            return img
        if x == 0 and y == 0:
            if -1*rangee < img[x][y][z] - img[x][y][z+1] < rangee:
                img[x][y].pop(z + 1)
                img[x][y].insert(z + 1, img[x][y][z])
            # if we complete green values, here it passes blue values
            return func(x, y, z+1)
        if x == 0 and y!=0:
            if -1*rangee < img[x][y][z] - img[x][y-1][z] < rangee:
                img[x][y - 1].pop(z)
                img[x][y - 1].insert(z, img[x][y][z])
            # here it goes left because we reached top of the colon
            return func3(x,y-1,z)
        if -1*rangee < img[x][y][z] - img[x - 1][y][z] < rangee:
            img[x - 1][y].pop(z)
            img[x - 1][y].insert(z, img[x][y][z])
        # it goes top from the bottom
        return func4(x-1,y,z)
    img_printer(func(0,0,0))
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

