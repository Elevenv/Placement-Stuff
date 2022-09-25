# def alpPattenr(n):
#     str1=""
#     for Row in range(0,n+1):    
#         for Col in range(0,n+1):     
#             if (((Row == 0 or Row == n-1) and Col >= 0 and Col <= n-1) or Row+Col==n-1):  
#                 str1=str1+str(Col+1)    
#             else:      
#                 str1=str1+" "    
#         str1=str1+"\n"    
#     print(str1); 

# n = int(input())
# alpPattenr(n)

n = int(input())
for i in range(n,0,-1):
    step = 0
    for j in range(0,n):
        if i==0 or i==n-1:
            print(j+1,end=" ")
        else:
            if step == 0:   
                print(" "*(i-1),i)
                step+=1
    # print('\n')