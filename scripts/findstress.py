import os

def readenergies():
    for filename in os.listdir("/home/fzysk/deepmd_workflow/output"):
        with open("/home/fzysk/deepmd_workflow/output/"+filename, "r") as input_file, open("/home/fzysk/deepmd_workflow/raw.dat", "a+") as output_file:
            for i,line in enumerate(input_file):
                if i==4 or i==5 or i==6:
                    print(line)
                    li=list(line.split())
                    for value,count in enumerate(li):
                        if value>0:
                            print(count)
                            output_file.write(count+" ")
            output_file.write("\n")
