import csv

users = []
loggedIn = ""
loggedInData = []
fakeToots = []
toots = []
pins = []
handle = []
name = []
followings = []
userPin = 0
followingNames = []
separateHandles = []

with open ('users.csv','r') as userFile:
    myFile = csv.reader(userFile)
    for row in myFile:
        handle.append(row[0])
        pins.append(row[2])
        name.append(row[1])
        followings.append(row[3])
        users.append(row)

pins.pop(0)
handle.pop(0)
name.pop(0)
followings.pop(0)
users.pop(0)


with open('toots.csv','r') as tootsFile:
    myFile = csv.reader(tootsFile)
    for row in tootsFile:
        fakeToots.append(row)
fakeToots.pop(0)


for i in range(0 ,len(fakeToots)):
    toots.append(fakeToots[i].split(","))

for i in toots:
    separateHandles.append(i[0])
print(separateHandles)


print("Enter your pin")
pin = input()
if pin in pins:
    print("Welcome,", handle[pins.index(pin)])
    loggedInData = users[pins.index(pin)]
        
else:
    print("Wrong pin, try again")

tootsShown = []
tootsData = []
tooterNames = []
tootHandles = []


    
def readToots():
    following = loggedInData[3].split('-')
    
    for i in range(0,len(following)):
       for j in range(0,len(toots)):
            if following[i] == toots[j][0]:
                tootsShown.append(toots[j][2])
                tootsData.append(toots[j])
            print(i,j)
            break

            
    for i in range(0,len(tootsData)):
        tootHandles.append(tootsData[i][0])
    for i in range(0,len(name)):
        for j in range(0,len(tootsData)):
            if tootHandles[j] == users[i][0]:
                tooterNames.append(users[i][1])
                break

    tooterNames.sort()
    tootsData.sort()
    print("Here's your toots :")    
    for toot in range(0,len(tootsData)):
        print(tooterNames[toot])
        print(tootsData[toot][0]) 
        print(tootsData[toot][1])
        print(tootsData[toot][2])

    
readToots()


