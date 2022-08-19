import os

def readenergies():
    i=1
    for filename in os.listdir("/home/fzysk/deepmd_workflow/output"):
        with open("/home/fzysk/deepmd_workflow/output/"+filename, "r") as input_file, open("/home/fzysk/deepmd_workflow/raw.dat", "a+") as output_file:
            real=0
            for line in input_file:
                if "N" in line:
                    li=list(line.split())
                    for value,count in enumerate(li):
                        if value>0:
                            print(count)
                            output_file.write(count+" ")
                            real=real+1
                if "C" in line:
                    li=list(line.split())
                    for value,count in enumerate(li):
                        if value>0:
                            print(count)
                            output_file.write(count+" ")
                            real=real+1
            output_file.write("\n")
            print(real)                
        i=1+1


