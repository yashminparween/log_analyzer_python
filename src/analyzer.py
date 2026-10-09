import os
folders=os.listdir("data/raw_logs")
valid_log=[]
Invalid_log=[]
for folder in folders:
    path=os.path.join("data","raw_logs",folder)
    with open(path,"r") as f:
        for lines in f:
            parts=lines.strip().split()
            print(parts)
            if len(parts)>=4:
                date=parts[0]
                time=parts[1]
                level=parts[2]
                message=" ".join(parts[3:])
                if level in["INFO","WARNING","ERROR"]:
                    valid_log.append(lines.strip())
                else:
                    Invalid_log.append(lines.strip())

            else:
                Invalid_log.append(lines.strip())
print(valid_log)
print(Invalid_log)

        