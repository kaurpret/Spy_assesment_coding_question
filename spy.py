def findSpy(number_of_people,has_information):
   if number_of_people>0 and len(has_information)<=number_of_people:
    for i in range(len(has_information)):
        for j in range(i):
            x=has_information[i][j]
            if x==number_of_people:
                return x
            else:
                return 0
    else:
        return has_information[0][0]
if __name__=='__main__':
    number_of_people=3
    has_information=[[1,2],[2,3]]
    print(findSpy(number_of_people,has_information))

