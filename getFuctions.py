import random as r
import mysql.connector as con


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


def getRandomID():  # not sure if it will work
    sqlMovie = "select movie_id from MOVIE"
    receiveMovieIDs = mycursor(sqlMovie)
    sqlTV = "select S_id from TV_SHOW"
    receiveTVIDs = mycursor(sqlTV)
    genID = str(r.randint(10000000000, 99999999999))
    for x in receiveMovieIDs:
        for j in receiveTVIDs:
            if x == genID and j == genID:
                return getRandomID()
    return genID


def getRandomAccount():  # not sure if it will work
    sql = "select account_number from CUSTOMER"
    receiveIDs = mycursor(sql)
    genID = str(r.randint(10000000000, 99999999999))
    for x in receiveIDs:
        if x == genID:
            return getRandomID()
    return genID


def getMovieInformation(mID):
    sql = "select M_name, genre, original, Dname from movie where movie_id = \"" + mID + "\""
    receivedMovie = mycursor(sql)
    print("\n\nMovie information: \n")
    if receivedMovie[0][2]:
        print("Netflix Original")
    print("Title: ", receivedMovie[0][0])
    print("Genre: ", receivedMovie[0][1])
    print("Director: ", receivedMovie[0][3])
    print("\n")


def getTVShowInformation(tvShowID):
    sql = "select S_name, genre, original, Dname, ep_number from tv_show where S_id = \"" + tvShowID + "\""
    receivedTVShow = mycursor(sql)
    print("\n\nTV Show information: \n")
    if receivedTVShow[0][2]:
        print("Netflix Original")
    print("Title: ", receivedTVShow[0][0])
    print("Genre: ", receivedTVShow[0][1])
    print("Director: ", receivedTVShow[0][3])
    print("Episode: ", receivedTVShow[0][4])
    print("\n")


def getDepartmentID():
    myquery = "select D.D_name, D.D_id from DEPARTMENT as D"
    i = int(1)
    getD = mycursor(myquery)
    for x in getD:
        print(i, ": ", x[0])
        i += 1
    departmentNum = int(input("Select a Department: "))
    departmentID = getD[departmentNum - 1][1]
    return departmentID


def getDirectorName():
    myquery = "select D.name from DIRECTOR as D"
    i = int(1)
    getname = mycursor(myquery)
    for x in getname:
        i += 1
        print(i, ": ", x[0])
    directorNum = int(input("select Director: "))
    directorName = getname[directorNum - 1][0]
    return directorName


def generateISP():
    genISP = int(r.randint(0, 4))
    listISP = ["321", "123", ["980"], ["111"], ["999"]]
    return listISP[genISP]


def checkUser(eAddress, password):
    sql = "select email, password from CUSTOMER"
    receivedQuarry = mycursor(sql)
    for x in receivedQuarry:
        if eAddress == x[0] and password == x[1]:
            return bool(1)
    return bool(0)


def checkAdmin(user, password):
    administrator = "admin"
    pass1 = "pass"
    return bool(pass1 == password and administrator == user)
