

def changeFile(file, inv, amount=0):
    f = open(file,"r+")
    inv = str(inv)
    word = ""
    words = []
    for line in f.readlines():
        if (line != "end"):
            for col in line:
                if(col != " "):
                    word += col
                else:
                    words.append(word)
                    word = ""
    f.close()
    i = -1
    for word in words:
        i+= 1
        print words[i]
        if (word == inv):
            i+=1
            words[i] = amount
            i=-1
            break
    f2 = open(file, "w+")
    f2.write("")
    f2.close()
    f3 = open(file, "a+")
    for word in words:
        i+= 1
        words[i] = str(words[i])+" "
        theword = words[i]
        f3.write(theword)
    f3.write("moduleEnd")
    f3.write("\n" +"end")
    f3.close()
    return

def readFile(file):
    f = open(file,"r+")
    word = ""
    words = []
    for line in f.readlines():
        if (line != "end"):
            for col in line:
                if(col != " "):
                    word += col
                else:
                    words.append(word)
                    word = ""
    f.close()
    return words

def rewrite(file, what):
    fo = open(file, "w+")
    fo.write(what)
    fo.close()
    return

def append(file,what):
    fo = open(file, "a+")
    fo.write(" " +what)
    fo.close()
    return

def save(player):
    player.savePlayer()

def load(player):
    player.loadPlayer()

def loadSpell1():
    infoArray = readFile("spells/p1.txt")
    spells = []
    spellcosts = []
    n=0
    for _ in infoArray:
        if(n%2 == 0):
            spells.append(infoArray[n])
        else:
            spellcosts.append(infoArray[n])
        n+=1
    n=0
    return spells, spellcosts