import mysql.connector as con
import getFuctions as getF
import MenuFucntions as men


def mycursor(sql):
    mydb = con.connect(
        host="localhost",
        user="rara",
        password="password",
        database="NETFLIX"
    )
    test = mydb.cursor()
    test.execute(sql)
    return tuple(test)


def HomeMenu():
    print("\n1. Movies")
    print("2. TV Shows")
    print("3. Show games")
    print("4. Logout")
    num = int(input("input: "))
    if num <= 0 or num >= 5:
        return HomeMenu()
    if num == 1:
        print("Movies section: ")
        i = int(1)
        match men.matchMTV():
            case 1:
                userInput = input("Enter the movie you would like to find: ")
                sql = "select * from MOVIE where M_name like \"%" + userInput + "%\""
                receiveMovie = mycursor(sql)
                if receiveMovie:
                    for x in receiveMovie:
                        print(i, ": ", x[1])
                        i += 1
                    selectedMovie = int(input("input: "))
                    while selectedMovie < 1 or selectedMovie > i:
                        selectedMovie = int(input("input invalid, try again stupid: "))
                    getF.getMovieInformation(receiveMovie[selectedMovie - 1][0])
                    return HomeMenu()
                else:
                    print("No movies found for", userInput)
                    return HomeMenu()
            case 2:
                sql = "select * from MOVIE"
                receiveMovie = mycursor(sql)
                if receiveMovie:
                    for x in receiveMovie:
                        print(i, ": ", x[1])
                        i += 1
                    selectedMovie = int(input("input: "))
                    while selectedMovie < 1 or selectedMovie > i:
                        selectedMovie = int(input("input invalid, try again stupid: "))
                    getF.getMovieInformation(receiveMovie[selectedMovie - 1][0])
                    return HomeMenu()
                else:
                    print("Netflix is too broke to have movies these days, blame management!")
                    return HomeMenu()
            case 3:
                sql = "select * from MOVIE where genre like \"%" + men.getGenre() + "%\""
                receiveMovie = mycursor(sql)
                if receiveMovie:
                    for x in receiveMovie:
                        print(i, ": ", x[1])
                        i += 1
                    selectedMovie = int(input("input: "))
                    while selectedMovie < 1 or selectedMovie > i:
                        selectedMovie = int(input("input invalid, try again stupid: "))
                    getF.getMovieInformation(receiveMovie[selectedMovie - 1][0])
                    return HomeMenu()
                else:
                    print("No Movies found for the selected genre")
                    return HomeMenu()
    elif num == 2:
        print("TV Shows section: ")
        i = int(1)
        match men.matchMTV():
            case 1:
                userInput = input("Enter the TV Show you would like to find: ")
                sql = "select * from TV_SHOW where S_name like \" like %" + userInput + "%\""
                receiveTVShow = mycursor(sql)
                if receiveTVShow:
                    for x in receiveTVShow:
                        print(i, ": ", x[1])
                        i += 1
                    selectedTVShow = int(input("input: "))
                    while selectedTVShow < 1 or selectedTVShow > i:
                        selectedTVShow = int(input("input invalid, try again stupid: "))
                    getF.getTVShowInformation(receiveTVShow[selectedTVShow - 1][0])
                    return HomeMenu()
                else:
                    print("No TV Shows found for ", userInput)
                    return HomeMenu()
            case 2:
                sql = "select * from TV_SHOW"
                receiveTVShow = mycursor(sql)
                if receiveTVShow:
                    for x in receiveTVShow:
                        print(i, ": ", x[1])
                        i += 1
                    selectedTVShow = int(input("input: "))
                    while selectedTVShow < 1 or selectedTVShow > i:
                        selectedTVShow = int(input("input invalid, try again stupid: "))
                    getF.getTVShowInformation(receiveTVShow[selectedTVShow - 1][0])
                    return HomeMenu()
                else:
                    print("Netflix is too broke to have movies these days, blame management!")
                    return HomeMenu()
            case 3:
                sql = "select * from TV_SHOW where genre like \"%" + men.getGenre() + "%\""
                receiveTVShow = mycursor(sql)
                if receiveTVShow:
                    for x in receiveTVShow:
                        print(i, ": ", x[1])
                        i += 1
                    selectedTVShow = int(input("input: "))
                    while selectedTVShow < 1 or selectedTVShow > i:
                        selectedTVShow = int(input("input invalid, try again stupid: "))
                    getF.getTVShowInformation(receiveTVShow[selectedTVShow - 1][0])
                    return HomeMenu()
                else:
                    print("No TV Shows found for the selected genre")
                    return HomeMenu()
    elif num == 3:
        sql = "select * from GAME"
        reecivedGame = mycursor(sql)
        if reecivedGame:
            for x in reecivedGame:
                print("name: ", x[1])
        return HomeMenu()
    elif num == 4:
        print("Logged out, New Shows will be waiting for you're return")
