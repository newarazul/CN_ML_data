import yaml
import json
import os
#read in the yaml file

with open("../data/poslows.yaml") as f:
    i=0
    structures=yaml.load_all(f)
    for structure in structures:
        i=i+1
#        print(i)
        with open("../data/structures/new%i.xyz" %i, "w") as th, open("../data/cells/cell%i.xyz" %i, "w") as tt, open("../data/dftinputs/dftinput%i.inp" %i, "w") as dftinput, open("../data/exampleinput.inp", "r") as example:
             print("32\n",file=th)
#            th.write(32)
             for keys,values in structure.items():
                y=values["cell"]
#                print(y)
                x=values["coord"]
                a=y[0]
                b=y[1]
                c=y[2]
#                print(z)
#                print(m)
#                print(m[2])
                d=a[0]
                e=a[1]
                f=a[2]
                print(d)
                print(f)
                g=b[0]
                h=b[1]
                j=b[2]
                k=c[0]
                l=c[1]
                m=c[2]
                print(d,e,f, file=tt)
                print(g,h,j, file=tt)
                print(k,l,m, file=tt)
             for line in example:
                    if line.strip()=="PROJECT":
                        print(line)
#                        dftinput.write(line.replace("Water", "new%i" %i))
                        print("\tPROJECT new%i" %i, file=dftinput)
#                        dftinput.write("\n")
                    if line.strip()=="!A":
                        print("\tA",d,e,f, file=dftinput)
                        print("\tB",g,h,j, file=dftinput)
                        print("\tC",k,l,m, file=dftinput)
                    if line.strip()=="COORD_FILE_NAME coord.xyz":
                        print("\tCOORD_FILE_NAME new%i.xyz" %i, file=dftinput)
                    else:
                        dftinput.write(line)

#                th.write(json.dumps(values["coord"]))
             for j in x:
                    a=j[0]
                    b=j[1]
                    c=j[2]
                    d=j[3]
#                    print(type(d))
                    print(d,a,b,c, file=th)
                    
#                    th.write(a,b,b,d)
#                print(values["coord"])
#                print(values["coord"],file=th)
