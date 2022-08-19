import os

def readenergies():
    for filename in os.listdir("/home/fzysk/deepmd_workflow/output"):
        with open("/home/fzysk/deepmd_workflow/output/"+filename, "r") as input_file, open("/home/fzysk/deepmd_workflow/raw.dat", "a+") as output_file:
            real=0
            for line in input_file:
                    li=list(line.split())
                    for value,count in enumerate(li):
                            print(count)
                            output_file.write(count+" ")
                            real=real+1
            output_file.write("\n")
            print(real)                


