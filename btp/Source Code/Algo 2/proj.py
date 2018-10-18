from csv_filereader import *
from weightage import *

def outer_main(alpha,beta,gamma,user_id):
    location = r'C:\Users\lenovo\Desktop\data_bridegroom.csv'
    data_bridegroom = read(location)

    location = r'C:\Users\lenovo\Desktop\data_bride.csv'
    data_bride = read(location)

    #print(data_bridegroom)
    #print("\n")
    #print(data_bride)
    #print(data)

    data_length = len(data_bride)
    no_of_keys = data_bride.keys()
    #print(no_of_keys)
    #print(data_length)

    n = user_id

    weightage_of_each_attribute = main(user_id)
    #weightage_of_each_attribute['Location']=0.5
    #weightage_of_each_attribute['Family']=0.25

    #print(weightage_of_each_attribute)

    '''user1_pref = { '10000' : { 'Family' :  'Rich_class',
                          'Location' : [ 'Metro', 'Urban'],
                          },
                   '1000' : { 'Family' :  'Upper_middle_class',
                          'Location' : 'semi_urban',
                          },
                   '100' : { 'Family' : 'middle_class',
                          'Location' :  'rural',
                          },
                  }

              
    user2 = { 'Family' : 'Upper_middle_class',
              'Location' :  'Metro'
            }
    '''

    '''if 'Metro' in data[n]['user_pref']['10000']['Location']:
        print(1)'''

    user1_pref = data_bridegroom[n]['user_pref']
    user2={}

    for x in no_of_keys:
        #print(x)
        #print("\n")
        user2[x] = data_bride[x]['user_details']
                    
        
    #print(user1_pref)
    #print("\n")
    #print(user2)

    #print(type(data[n]['user_pref']['10000']['Location']))
    #print(type(user1_pref['10000']['Location']))

    count_10000=0
    count_100=0
    count_1=0

    attr_10000=[]
    attr_100=[]
    attr_1=[]

    score = {}
    score12 = 0
    Anything = 'Anything'

    for x in no_of_keys:
            for y in user2[x].iteritems():
                a,b = y
                #print(a,b)
                if user1_pref['10000'][a] == Anything or b in user1_pref['10000'][a] :
                    count_10000=count_10000+1
                    attr_10000.append(a)
                elif user1_pref['100'][a] == Anything or b in user1_pref['100'][a]  :
                    count_100=count_100+1
                    attr_100.append(a)
                elif user1_pref['1'][a] == Anything or b in user1_pref['1'][a]  :
                    count_1=count_1+1
                    attr_1.append(a)
            
            print(attr_10000)
            print(attr_100)
            print(attr_1)

            print(count_10000)
            print(count_100)
            print(count_1)
                
            for p in attr_10000:
                #print(x)
                score12 = score12 + alpha * weightage_of_each_attribute[p]
                #print(score12)

            for q in attr_100:
                #print(x)
                score12 = score12 + beta * weightage_of_each_attribute[q]
                #print(score12)

            for r in attr_1:
                #print(x)
                score12 = score12 + gamma * weightage_of_each_attribute[r]
                #print(score12)

            score[x] = score12
            score12 = 0
            attr_10000=[]
            attr_100=[]
            attr_1=[]
            count_10000=0
            count_100=0
            count_1=0
            #print(score12)
    return (score)
            
y='Y'
Y='Y'

n='N'
N='N'

want_rec = input("Want Recommendations")
print(want_rec)
if want_rec == 'Y':
    number = input("Recommendations of what user id want to see..??")

    '''LEVEL 1 : (10000,100,1)'''
    
    rec = outer_main(10000,100,1,number)
    print(rec)
    index=0
    string = str(input("Want more recommendations ? (Press Y/N for yes/no)"))
    print(string)

    if string == 'Y':
        index=1

        '''LEVEL 2 : (100,10,1)'''
        
        rec=outer_main(100,10,1,number)
        print(rec)

    if index==1:
        string = input("Want further more recommendations ? (Press Y/N for yes/no)")
        if string == 'Y':

            '''LEVEL 3 : (16,4,1)'''
            
            rec=outer_main(16,4,1,number)
            print(rec)

        string = input("Want further more more recommendations ? (Press Y/N for yes/no)")
        if string == 'Y':

            '''LEVEL  : (4,2,1)'''
            
            rec=outer_main(4,2,1,number)
            print(rec)
            
    
        

    
    
        
    
    
    
    


#print(attr_10000)
#print(attr_1000)
#print(attr_100)
  
#print(count_10000)
#print(count_1000)
#print(count_100)



    


        
        


        
        
    
    
    
