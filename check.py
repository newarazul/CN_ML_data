import os
import numpy as np

def loadbasestructure():
    coord=[]
    with open("/home/fzysk/deepmd_workflow/base.xyz") as basefile:
        coords=basefile.readlines()[2:]
        for count in coords:
            a=np.append(count[2:])
        b=np.array(coords)
        print(b)

#            print(type(count))
#        a=np.array(coords)
#        print(a.shape)
#        a=np.delete(a, np.arange(0, a.size, 3))
#        print(a)


#check against all other coords
#def checkagainstbase():
#    for filename in os.listdir("/home/fzysk/deepmd_workflow/data/structures"):
#        with open("/home/fzysk/deepmd_workflow/data/structures/"+filename, "r") as input_file:
#            coords2=input_file.readlines()[2:]
             
    

#def checktest():
#    i=1
#    for filename in os.listdir("/home/fzysk/deepmd_workflow/output"):
#        with open("/home/fzysk/deepmd_workflow/output/"+filename, "r") as input_file, open("/home/fzysk/deepmd_workflow/raw.dat", "a+") as output_file:
#            real=0
#            for line in input_file:
#                if "N" in line:
#                    li=list(line.split())
#                    for value,count in enumerate(li):
#                        if value>0:
#                            print(count)
#                            output_file.write(count+" ")
#                            real=real+1
#                if "C" in line:
#                    li=list(line.split())
#                    for value,count in enumerate(li):
#                        if value>0:
#                            print(count)
#                            output_file.write(count+" ")
#                            real=real+1
#            output_file.write("\n")
#            print(real)                
#        i=1+1


