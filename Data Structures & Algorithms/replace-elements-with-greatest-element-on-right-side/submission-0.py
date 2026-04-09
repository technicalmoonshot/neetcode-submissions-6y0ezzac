class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        res =[0] * len(arr)
        res_max = -1

        for i in range(len(arr)-1, -1, -1):
            res[i]=res_max
            res_max = max(res_max, arr[i])
        return res


 




   


        