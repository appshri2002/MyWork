################################################################################
# Author: Apoorva Shrivastava
# Date:3/29/21
# Description ...
'''
In this code we have three functions that will be called in main.
We tests squares to see if they are magic.
We used list functions, return functions,call functions, if-else
for loops.
'''
################################################################################

#define function to be called
def print_square(m):


#to print numbers in square form
    for i in range(0,3):

        word=""

        for j in range(0,3):

            word+=str(m[i][j])+" "
        print(word.strip())

#defined to be called.
def allNumbers(m):
    result=True

    #create empty list
    c=list()
    for i in range(0,3):
        for j in range(0,3):
            c.append(m[i][j])

    A = [1,2,3,4,5,6,7,8,9]

    for i in A:
        if i in c:
            continue
        else:
            result=False
    return result
#defined to be called
def is_magic(m):
#calling function.
    if (allNumbers(m)):
#checking validity of function
        if (m[0][0]+m[0][1]+m[0][2]==15 and m[1][0]+m[1][1]+m[1][2]==15 and m[2][0]+m[2][1]+m[2][2]==15) and (m[0][0]+m[1][0]+m[2][0]==15 and m[0][1]+m[1][1]+m[2][1]==15 and m[0][2]+m[1][2]+m[2][2]==15) and (m[0][0]+m[1][1]+m[2][2]==15 and m[0][2]+m[1][1]+m[2][0]==15):
                    return True
        else:
            return False
    else:
        return False

#defining main function.
def main():

    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    m2 = [[5, 5, 5], [5, 5, 5], [5, 5, 5]]
    m3 = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]


    print("Your square is:")

    print_square(m1)
    if is_magic(m1):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not a Lo Shu magic square.")
        print()

        print("Your square is:")

        print_square(m2)
        if is_magic(m2):
            print("It is a Lo Shu magic square!")
        else:
            print("It is not a Lo Shu magic square.")
            print()

    print("Your square is:")

    print_square(m3)
    if is_magic(m3):
        print("It is a Lo Shu magic square!")
    else:
        print("It is not Lou Shou magic.")


if __name__ == '__main__':
    main()
