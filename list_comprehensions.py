def run():
    #squares = []
    #for i in range(1, 101):
        #squares.append(i**2)
    #print(squares)
    #squares = [1**2 for i in range(1, 101) if i % 3 !=0]
        # print(squares)
    squares = [i**2 for i in range(1,101) if i % 3 !=0]
    #[element for in iterable if condition]

    print(squares)

if __name__ == '__main__':
    run()
