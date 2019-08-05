try:
    with open("u_data.txt") as f:
        lines=f.readlines()
        new_list=[]
        for line in lines:
            line=line.replace