import mysql.connector as con
import getFuctions as getF
import MenuFucntions as men
import homeMenuFunction as LoggedIn


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


def updateMycursor(sql):
    mydb = con.connect(
        host="localhost",
        user="rara",
        password="password",
        database="NETFLIX"
    )
    test = mydb.cursor()
    test.execute(sql)
    mydb.commit()


def adminMovies():
    print("1. Add Movies")
    print("2. Remove Movies")
    print("3. Go back")
    userInput = int(input("Input: "))
    if userInput == 1:
        movieName = input("Enter Movie name: ")
        length = input("Enter Movie length in minutes: ")
        genre = str(men.getGenre())
        original = input("Is Movie original TRUE/FALSE: ")
        size = input("Enter Movie size MB/GB: ")
        m_ID = str(getF.getRandomID())
        d_ID = str(getF.getDepartmentID())
        dName = str(getF.getDirectorName())
        sql = "INSERT INTO MOVIE VALUES (" + "\"" + m_ID + "\", \"" + movieName + "\"," + length + ",\"" + dName + "\"," + size + ",\"" + genre + "\"," + original + ",\"" + d_ID + "\")"
        try:
            updateMycursor(sql)
        except NameError:
            print("Unable to add movie")
        return adminMovies()
    elif userInput == 2:
        sql = "select movie_id ,M_name, Dname, original from MOVIE"
        receiveMovie = mycursor(sql)
        i = int(1)
        for x in receiveMovie:
            print(i, ": ", x[1], " ", x[2], " ", x[3])
            i += 1
        selectedMovie = int(input("Select movie to remove: "))
        movieId = receiveMovie[selectedMovie - 1][0]
        sql = "DELETE FROM MOVIE WHERE movie_id=" + "\"" + movieId + "\""
        try:
            updateMycursor(sql)
            print("delete complete")
        except NameError:
            print("Unable to remove movie")
        return adminMovies()
    elif userInput == 3:
        match men.AdminMenu():
            case 1:
                adminMovies()
            case 2:
                adminTVShow()
            case 3:
                program()
    else:
        adminMovies()


def adminTVShow():
    print("1. Add TV Show")
    print("2. Remove TV Show")
    print("3. Go back")
    userInput = int(input("Input: "))
    if userInput == 1:
        tvName = input("Enter TV Show name: ")
        ep_number = input("Enter TV Show episode number in: ")
        genre = men.getGenre()
        original = input("Is TV Show original TRUE/FALSE: ")
        size = input("Enter TV Show size MB/GB: ")
        s_ID = str(getF.getRandomID())
        d_ID = str(getF.getDepartmentID())
        dName = str(getF.getDirectorName())
        sql = "INSERT INTO TV_SHOW VALUES (" + "\"" + s_ID + "\", \"" + tvName + "\"," + original + "," + size + "," + ep_number + ",\"" + dName + "\",\"" + genre + "\",\"" + d_ID + "\")"
        try:
            updateMycursor(sql)
        except NameError:
            print("Unable to add TV Show")
        return adminTVShow()
    elif userInput == 2:
        sql = "select S_id, S_name, Dname, original from TV_SHOW"
        receiveTV = mycursor(sql)
        i = int(1)
        for x in receiveTV:
            print(i, ": ", x[1], " ", x[2], " ", x[3])
            i += 1
        selectedTv = int(input("Select TV Show to remove: "))
        tvId = receiveTV[selectedTv - 1][0]
        sql = "DELETE FROM TV_SHOW WHERE S_id=" + "\"" + tvId + "\""
        try:
            updateMycursor(sql)
            print("delete complete")
        except NameError:
            print("Unable to remove TV Show")
        return adminTVShow()
    elif userInput == 3:
        match men.AdminMenu():
            case 1:
                adminMovies()
            case 2:
                adminTVShow()
            case 3:
                program()
    else:
        adminTVShow()


def NewUser():
    account_number = getF.getRandomAccount()
    firstname = str(input("Enter you're first name: "))
    lastname = str(input("Enter you're last name: "))
    subtype = men.getSubType()
    address = str(input("Enter your address: "))
    isp = getF.generateISP()
    email_address = input("Enter your email: ")
    phone = str(input("Enter you phone number 000-000-0000: "))
    country = men.getCountry(isp)
    password = str(input("Enter a 10 character password: "))
    try:
        sql = "INSERT INTO CUSTOMER VALUES (\"" + account_number + "\",\"" + firstname + "\",\"" + lastname + "\",\"" + subtype + "\",\"" + address + "\",\"" + isp + "\",\"" + email_address + "\",\"" + phone + "\",\"" + country + "\",\"" + password + "\")"
        updateMycursor(sql)
        print("Welcome to Netflix")
    except NameError:
        print("Failed to add new user")


def NetflixHome():
    user = input("Enter email: ")
    password = input("Enter password: ")
    if getF.checkAdmin(user, password):
        match men.AdminMenu():
            case 1:
                adminMovies()
            case 2:
                adminTVShow()
    elif getF.checkUser(user, password):
        LoggedIn.HomeMenu()
    else:
        print("Invalid email address or password")


def program():
    LoginSelection(men.LoginMenu())


def LoginSelection(num):
    match num:
        case 1:
            NetflixHome()
            program()
        case 2:
            NewUser()
            program()


program()
