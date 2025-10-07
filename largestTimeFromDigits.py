class Solution:
    
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        #TAKE THE MINIMUM TIME POSSIBLE
        self.maxTime = "00:00"

        #TAKE A STATUS VARIABLE WHICH WILL TELL US IF WE FOUND OUR ANSWER OR NOT
        self.stat = False

        # APPROACH IS TO SORT THE ARRAY IN DESCENDING ORDER AND THEN CREATE PERMUTATIONS, THIS WILL HELP US REACH THE ANSWER FAST
        Map  ={}
        arr.sort(reverse=True)
        for i in range(len(arr)):
            Map[i]=0
        
        def perm(ans):
            if len(ans)==4:
                hr = ''.join(ans[:2])
                mm = ''.join(ans[2:])
                time = hr+':'+mm
                t1 = int(hr)
                t2 = int(mm)
                if t1<=23 and t2<=59:
                    #IF TIME IS VALID ONLY THEN COMPARE
                    if t1>=int(self.maxTime[:2]):
                        if t2>=int(self.maxTime[3:]):
                            self.maxTime = time
                            self.stat = True

                return

            # RETURN IF WE FOUND OUR ANSWER
            if self.stat == True:
                return
            
            for i in range(0, len(arr)):
                if Map[i]!=1:
                    Map[i]=1
                    ans.append(str(arr[i]))
                    perm(ans)
                    # RETURN IF WE FOUND OUR ANSWER
                    if self.stat == True:
                        return
                    Map[i]=0
                    ans.pop()
        perm([])
        
        if self.maxTime!="00:00" or(self.maxTime=="00:00" and self.stat==True):
            return (self.maxTime)
        else:
            return ""
