def LoginMenu():
    print("\n1. Login")
    print("2. New User")
    num = int(input("input: "))
    if num <= 0 or num >= 3:
        return LoginMenu()
    return num


def matchMTV():
    print("\n1. Search")
    print("2. show all")
    print("3. Filter")
    num = int(input("input: "))
    if num <= 0 or num >= 4:
        return matchMTV()
    return num


def AdminMenu():
    print("\n1. Movies")
    print("2. TV shows")
    print("3. Logout")
    num = int(input("input: "))
    if num <= 0 or num >= 4:
        return AdminMenu()
    return num


def getGenre():
    print("Enter Movie genre")
    print("1 crime")
    print("2 fantasy")
    print("3 Romance")
    print("4 Action")
    print("5. Adventure")
    print("6. Drama")
    print("7. Comedy")
    print("8. Science Fiction")
    print("9. War")
    print("10. Western")
    user = int(input("input: "))
    if user <= 0 or user >= 10:
        return getGenre()
    match user:
        case 1:
            return "Crime"
        case 2:
            return "Fantasy"
        case 3:
            return "Romance"
        case 4:
            return "Action"
        case 5:
            return "Adventure"
        case 6:
            return "Drama"
        case 7:
            return "Comedy"
        case 8:
            return "Science Fiction"
        case 9:
            return "War"
        case 10:
            return "Western"


def getSubType():
    print("Select a plan")
    print("1. Basic")
    print("2. Standard HD")
    print("3. HD4K")
    userinput = int(input("input: "))
    if userinput <= 0 or userinput >= 4:
        return getSubType()
    match userinput:
        case 1:
            return "Basic"
        case 2:
            return "Standard HD"
        case 3:
            return "HD4K"


def getCountry(isp):
    match isp:
        case "321":
            return "USA"
        case "123":
            return "Canada"
        case "980":
            return "UK"
        case "111":
            return "Japan"
        case "999":
            return "France"
