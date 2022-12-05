# day 3


test =["vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw"]

sum=0



# https://adventofcode.com/2022/day/3

inputFile = 'input/03_input'
   
with open(inputFile) as input:
        for row in input:
            r=row.strip()
            print(len(r))
            l = int(len(r)/2)
            print(l)
            c1 = r[0:l]
            c2 =  r[l:]
            print(c1,c2)
    
            for c in c1:
       # print(c)
       # print(c2.find(c))
                if c2.find(c)>-1:
                    s=(ord(c) - ord('A') + 27 if c<='Z' else ord(c) - ord('a')+1)
                    sum+=s
                    print(c)
                    print("s",s)
                    break
                    
                    
                    
                    
                    
print("Day3 part1:",sum)


rowlist =[]
sum=0
#for row in test:
with open(inputFile) as input:
        for row in input:
            rowlist.append(row)
            
            
for i in range(0,len(rowlist),3):
        print(i)
        c1=rowlist[i]
        c2=rowlist[i+1]
        c3=rowlist[i+2]
        
        print(c1,c2,c3)
        
        for c in c1:
        
       # print(c2.find(c))
                if c2.find(c)>-1 and c3.find(c)>-1:
                    s=(ord(c) - ord('A') + 27 if c<='Z' else ord(c) - ord('a')+1)
                    sum+=s
                    print(c,s)
                    break
                    
                    
print("Day3 part2:",sum)
            
            
            

            
            