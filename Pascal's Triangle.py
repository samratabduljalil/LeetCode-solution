class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numslist=[]
        list1=[]
        for i in range(1,numRows+1):
            list2=[]
            for j in range(i):
                if j==0 or j==i-1:
                    list2.append(1)
                else:
                  if j<=len(list1)-1:
                    Sum=list1[j-1]+list1[j]
                    list2.append(Sum)
            numslist.append(list2)
            list1=[]
            for l in list2:
                list1.append(l)  
        return numslist