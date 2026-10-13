import csv
import os
import shutil
folders=os.listdir("data/raw_logs")
data=["INFO","WARNING","ERROR"]
clean_data=[]
for folder in folders:
    path=os.path.join("data/raw_logs",folder)
    if not os.path.isfile(path):
        continue
    is_valid=True
    with open(path,"r") as f:
        content=f.readlines()
        for lines in content:
            line=lines.strip().split()
            if(len(line)<4):
                is_valid=False
                break
            date=line[0]
            time=line[1]
            level=line[2]
            if(level not in data):
                is_valid=False
                break
            message=" ".join(line[3:])
            clean_data.append([date,time,level,message])
    print(clean_data)
    if is_valid:
        # filename=os.path.splitext(folder)[0]+".csv"
        # destination=os.path.join("data/cleaned",filename)
        with open("data/cleaned/clean.csv","w") as f:
            writer=csv.writer(f)
            writer.writerow(["Date","Time","Level","Message"])
            writer.writerows(clean_data)
            

    else:
        destination = os.path.join("data/quarantine",folder)
        shutil.move(path, destination)
        print(path, "-> Quarantine folder")
        




    
    



           

        