students = {}

def test():
    num = int(input())
    # print(num)
    for i in range(0,num):
        line = input()
        # print(line)
        tokens = line.split()
        print(tokens)
        # students["NCTU-1"]=2000
        '''
        students[tokens[0]+"-1"] = int(tokens[1])
        students[tokens[0]+"-2"] = int(tokens[2])
        students[tokens[0]+"-3"] = int(tokens[3])
        students[tokens[0]+"-4"] = int(tokens[4])
        '''
    for j in range(1,5):
        students[tokens[0]+"-"+str(j)] = int(tokens[j])
    # print(students)
    num = int (input())
    # print(num)
    for i in range(0,num):
        line = input()
        #print(line, students[line])
        print(line, students.get(line))
    #print("Stanford-1",students["Standford-1"])
    print("Stanford-1", students.get("Stanford-1"))



    
test()