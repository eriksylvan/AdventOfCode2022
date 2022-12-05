# day 4




# https://adventofcode.com/2022/day/4

inputFile = 'input/04_input'
#inputFile = 'input/04_test_input'
count =0
with open(inputFile) as input:
        for row in input:
            s=row.strip().replace(',','-').split('-')
            for i in range(4):
                s[i]=int(s[i])
            print(s)
            if (s[0]<=s[2] and s[1]>=s[3] ) or (s[2]<=s[0] and s[3]>=s[1] ):
                count +=1
                print(s)
                
                
print("Day4 part1:",count)            

inputFile = 'input/04_input'
#inputFile = 'input/04_test_input'
count =0
with open(inputFile) as input:
        for row in input:
            s=row.strip().replace(',','-').split('-')
            for i in range(4):
                s[i]=int(s[i])
            if (s[0]<=s[2] and s[1]>=s[3] ) or (s[2]<=s[0] and s[3]>=s[1] ) or (s[0]<=s[2] and s[1]>=s[2] )or (s[0]<=s[3] and s[1]>=s[3] ) or (s[2]<=s[0] and s[3]>=s[0] ) or (s[2]<=s[1] and s[3]>=s[1] ):
             
             
             
                count +=1
                print(s)    




print("Day4 part2:",count)                
            
                
            
            
