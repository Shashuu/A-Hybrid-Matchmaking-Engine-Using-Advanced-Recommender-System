import csv

def read(s):
    #print('one')
    user={}
    user_pref = {}
    user_details = {}
    result={}
    dictionary10000 = {}
    dictionary100 = {}
    dictionary1 = {}
    p = open(s,'r')
    reader = csv.reader(p)

    for col in reader:
        y = int(col[0])
        break
    
    #print(y)
    
    with open(s,'r') as l:
        #print('two')

        reader = csv.reader(l)
        
        for rows in reader:
            #print(type(rows[0]),type(y))
            if rows[0] is not '' and int(rows[0]) is int(y)  :
                #print('three')
                #print(rows[0])
                if rows[1] is not '':
                    #print(rows[1])
                    user_details[rows[1]] = rows[2]
                    #print(user_details)
                
                x = rows[3]
                #print(x)
                if x == '10000':
                   dictionary10000[rows[4]] = rows[5]
                if x == '100':
                   dictionary100[rows[4]] = rows[5]
                if x == '1':
                   dictionary1[rows[4]] = rows[5]
                
                #print(dictionary10000)
                #print(dictionary1000)
                #print(dictionary100)
                   #print(list1)
                   

            elif rows[0] is not '' :
                #print('four')
                user_pref['10000'] = dictionary10000
                user_pref['100'] = dictionary100
                user_pref['1'] = dictionary1
                

                #print(user_pref)
                #print(user_details)
                                
                user['user_details'] = user_details
                user['user_pref'] = user_pref

                #print(user)
                
                #print(user_details)
                #print(user_pref)
                
                result[y] = user
                
                #print(list1)
                                
                                
                user_pref = {}
                user_details = {}
                user={}

                dictionary10000 = {}
                dictionary100 = {}
                dictionary1 = {}
                
                
                #print(list1)

                #print(type(rows[0]))
                y = int(rows[0])
                
                if rows[1] is '':
                     return(result)
                    
                user_details[rows[1]] = rows[2]
                
                x = rows[3]
                #print(x)
                if x == '10000':
                   dictionary10000[rows[4]] = rows[5]
                if x == '100':
                   dictionary1000[rows[4]] = rows[5]
                if x == '1':
                   dictionary100[rows[4]] = rows[5]
                
                #print(result)
                #print((y))
                     
    return(result)        


#x= read('C:\Users\lenovo\Desktop\data_bride.csv')
#print(x)

#x= read('C:\Users\lenovo\Desktop\data_bridegroom.csv')
#print(x)

        
        




