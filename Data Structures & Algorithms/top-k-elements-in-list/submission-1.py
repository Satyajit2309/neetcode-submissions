class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        result = []


        for num in nums:
            if num in dictionary:
                dictionary[num] += 1
            else:
                dictionary[num]=1

        frequency = sorted(dictionary.items() , key=lambda item:item[1] , reverse= True)

        for key , value in frequency:
            result.append(key)
        
        return result[:k]

