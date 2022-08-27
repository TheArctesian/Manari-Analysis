from coalas import csvReader as c

def test():
    print("JELLO WORLD")
if __name__ == "__main__":
    all = []
    with open('./Minari-Screenplay.txt', 'r') as f:
        for line in f: 
            all.append(line)
    names = []
    line = []
    for i in range(len(all)):
        if (i %2)==0:
            names.append(all[i].strip())
        if (i %2)!=0:
            line.append(all[i].strip())

    print(len(names))
    print(len(line))
    
    colsN = ["Character","Line","Language","LangInt"]
    c.createCSV(colsN)
    c.Character = names
    c.Line = line
    for l in line:
        if l[:1] == '[':
            c.Language.append("Korean")
            c.LangInt.append(0)
        else: 
            c.Language.append("English")
            c.LangInt.append(1)

    c.writeCSV("Script.csv")
