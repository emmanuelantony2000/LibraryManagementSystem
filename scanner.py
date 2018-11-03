#num = 3
def scan():
    num = 3
    #return [[str(input()) for _ in range(num-1)].append(int(input()))]
    a = [str(input()) for _ in range(num)]
    #a.append(int(input()))
    return a

#the columns are in the following order
#Name, Author, Book code, No of books available

#num = 4
def enter():
    num = 4
    a = [str(input()) for _ in range(num)]
    return a

#the columns are in the following order
#Name, Class, ID, Date Taken, Return Date
