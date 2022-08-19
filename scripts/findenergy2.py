import os

def readenergies():
    i=1
    for filename in os.listdir("/home/fzysk/deepmd_workflow/output"):
        with open("/home/fzysk/deepmd_workflow/output/"+filename, "r") as input_file, open("/home/fzysk/deepmd_workflow/raw.dat", "a+") as output_file:
            for line in input_file:
                if "ENERGY|" in line:
                    l=[]
                    for t in line.split():
                        try:
                            l.append(float(t))
                        except ValueError:
                            pass
                    output_file.write(t+"\n")
        i=1+1


