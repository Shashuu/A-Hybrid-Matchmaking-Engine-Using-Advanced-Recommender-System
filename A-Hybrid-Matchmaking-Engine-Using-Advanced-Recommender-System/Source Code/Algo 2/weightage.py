import csv
from numpy import *

#13 itemslist is sent from proj file to get the weightage of 10 attributes

def weighing(priority_list):
   length=len(priority_list)
   matrix_index= {}
   priority_index = length


   for x in range(length):
      matrix_index[priority_list[x]]= priority_index 
      priority_index = priority_index - 1

   #print(matrix_index)
   #print(priority_index)
       
   a=[]

   for x in range(length):
           a.append([])
           for y in range(length):
               a[x].append(1)

   #print(a)

   for x in range(length):
       for y in range(0,x+1):
           if x!=y :
              (p,q) = (priority_list[x],priority_list[y])
              #print(p,q)
              if (matrix_index[p] - matrix_index[q]) <0 :
                 a[y][x] = 1/float((matrix_index[q] - matrix_index[p])+1)
               
              else :
                  a[y][x] = (matrix_index[p] - matrix_index[q])+1
               
               
              a[x][y] = ( 1 / float(a[y][x]))
              #print(a)

   #print(a)

   sum_row = [0]*length
   sum_column = [0] * length

   for x in range(length):
      for y in range(length):
         sum_row[x] = sum_row[x] + a[y][x]
         
   #print(sum_row)

   for x in range(length):
      for y in range(length):
         a[x][y] = a[x][y]/sum_row[y]

   for x in range(length):
      for y in range(length):
        sum_column[x] =  sum_column[x] + a[x][y]/float(length)


   #print(a)
   #print(sum_row)
   #print(sum_column)
     
   #sum_col = sum(sum_column)
   #print(sum_col)

   #for x in range(length):
     # sum_column[x] = sum_column[x]/sum_col

   return(sum_column)


def main(user_id):
   l = open(r'C:\Users\lenovo\Desktop\data.csv','r')

   reader = csv.reader(l)
   all_list=[]
   all_attr_list=[]

   for rows in reader:
      if rows[6] is not '':
         all_attr_list.append(rows[9:19])
         a = []
         a.append(rows[0])
         group = rows[6:9]
         a.append(group)
         subgrouping_1 = rows[9:11]
         a.append(subgrouping_1)
         subgrouping_2 = rows[11:14]
         a.append(subgrouping_2)
         subgrouping_3 = rows[14:19]
         a.append(subgrouping_3)
         all_list.append(a)
         #print(all_attr_list)

   n = user_id
   #print(all_list[n][0])
   group_weigh = weighing(all_list[n-1][1])
   
   subgrouping_1_weigh = weighing(all_list[n-1][2])
   subgrouping_2_weigh = weighing(all_list[n-1][3])
   subgrouping_3_weigh = weighing(all_list[n-1][4])

   '''group_weigh = array(group_weigh)
   subgrouping_1_weigh = array(subgrouping_1_weigh)
   subgrouping_2_weigh = array(subgrouping_2_weigh)
   subgrouping_3_weigh = array(subgrouping_3_weigh)

   subgrouping_1_weigh = group_weigh[0]*subgrouping_1_weigh
   subgrouping_2_weigh = group_weigh[1]*subgrouping_2_weigh
   subgrouping_3_weigh = group_weigh[2]*subgrouping_3_weigh'''

   attr_weightage=[]
   dummy= []

   for x in range(len(subgrouping_1_weigh)):
      attr_weightage.append(group_weigh[2]*subgrouping_1_weigh[x])
   attr_weightage.reverse()

   for x in range(len(subgrouping_2_weigh)):
      dummy.append(group_weigh[1]*subgrouping_2_weigh[x])
   dummy.reverse()
   attr_weightage =attr_weightage + (dummy)

   dummy=[]
   
   for x in range(len(subgrouping_3_weigh)):
      dummy.append(group_weigh[0]*subgrouping_3_weigh[x])
   
   dummy.reverse()
   attr_weightage =attr_weightage + (dummy)
   
   #print(attr_weightage)

   #print(group_weigh,subgrouping_1_weigh,subgrouping_2_weigh,subgrouping_3_weigh)
   attr_weightage_dict ={}

   attributes_count = len(all_attr_list[n-1])
   #print(attributes_count)
   for x in range(attributes_count):
      attr_weightage_dict[all_attr_list[n-1][x]] = (attr_weightage[x])

   return(attr_weightage_dict)

if __name__ == "__main__":
   x=main(1)
   print(x)
    
