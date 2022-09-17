import os

with open("../dftinputs/example.txt") as f:
    for filename in os.listdir("C:/Users/Frederik/PycharmProjects/creat_structures/data/structures"):
  #      print(filename)
  #      print(type(filename))
 #       print(filename.strip(".xyz"))
        filename=filename.strip(".xyz")
#        print(filename)
        with open("../dftinputs/inputs_all/"+filename+".txt", "w") as t:
            for line in f:
                print(line)
                t.write(line.replace("structurex.xyz", filename+".xyz"))
                t.write("hallo")
                print(filename)
