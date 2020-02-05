ShelfSpace = 25
CozonacShelf = []
LMC = 4
CreatedCozonac = []


def make():
    if len(CreatedCozonac) >= LMC: 
        print ("you can only make 4 cozonacs at a time :/")
        return
    CreatedCozonac.append(1)
    print ("cozonac made")


def store():
    if len(CozonacShelf) >= ShelfSpace:
        print ("you can only store 25 cozonacs, you have to throw or eat it :/")
        return
    if len(CreatedCozonac) == 0:
        print ("you cant store cozonacs you dont have :/")
        return
    CreatedCozonac.pop()
    CozonacShelf.append(1)
    print ("cozonac stored")


def count():
    x = eval(input("What cozonac you want to count? (stored or created only) "))
    x.lower()
    if x == "stored":
        print (len(CozonacShelf))
    elif x == "created only":
        print (len(CreatedCozonac))
    else:
        print ('try typing ', '"stored " or', '"created only "')


def eat():
    if len(CreatedCozonac) > 0:
        CreatedCozonac.pop()
        print ("tasty :p")
    elif len(CozonacShelf) > 0:
        CozonacShelf.pop()
        print ("tasty :p")
    elif len(CozonacShelf) == 0 and len(CreatedCozonac) == 0:
        make()
        CreatedCozonac.pop()
        print ("tasty :p")


def throw():
    if len(CozonacShelf) > 0:
        CozonacShelf.pop()
        print ("cozonac thrown succesfully")
    else:
        print ("you cant throw cozonacs if you dont have any")

def main():
    cmd = eval(input("what do you want to do? (make, eat, throw, count, store, quit)"))
    while(cmd != "quit"):
        if cmd == "make":
            make()
        elif cmd == "eat":
            eat()
        elif cmd == "throw":
            throw()
        elif cmd == "count":
            count()
        elif cmd == "store":
            store()
        elif cmd == "quit":
            print ("goodbye")
        cmd = eval(input("what do you want to do? (make, eat, throw, count, store, quit)"))
        

main()


print ("CreatedCozonac", CreatedCozonac)
print ("cozonacShelf", CozonacShelf)
