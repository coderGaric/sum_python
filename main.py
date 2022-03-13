class Solution:
    def __init__(self, list_to_solve):
        self.list_to_solve = list_to_solve
        self.length = len(list_to_solve)

    @property
    def result(self):
        str = ""
        for i in range(self.length):
            li = self.list_to_solve[i]["nums"]
            tg = self.list_to_solve[i]["target"]
            str += f"List: {li}\nTarget: {tg} \
            \n-------------- TWO SUM -------------- \
            \nResult(nested for loop): {self.two_sum_nested(li, tg)} \
            \nResult(for nested while loop): {self.two_sum_while(li, tg)}\
            \n------------- THREE SUM ------------- \
            \nResult(nested for loop): {self.three_sum_nested(li, tg)} \
            \nResult(for nested while loop): {self.three_sum_while(li, tg)}\
            \n------------- FOUR SUM ------------- \
            \nResult(nested for loop): {self.four_sum_nested(li, tg)} \
            \nResult(for nested while loop): {self.four_sum_while(li, tg)}\n\n"
        return str
    
    """ 2SUM """
    def two_sum_nested(self, li, tg):
        li.sort()
        length = len(li)
        result = []
        
        for i in range(length):
            for j in range(length):
                if i != j and li[i] + li[j] == tg:
                    temp = sorted([li[i], li[j]])
                    if temp not in result:
                        result.append(temp)
        return result

    def two_sum_while(self, li, tg):
        li.sort()
        length = len(li)
        result = []

        for i in range(length - 1):
            if i > 0 and li[i] == li[i - 1]:
                continue
                
            right = length - 1

            while (i < right):
                sum = li[i] + li[right]
                if sum < tg or sum > tg:
                    right -= 1
                else:
                    result.append([li[i], li[right]])
                    while right > 0 and li[right] == li[right - 1]:
                        right -= 1
                    right -= 1
        return result
                    
    """ 3SUM """
    def three_sum_nested(self, li, tg):
        li.sort()
        length = len(li)
        result = []
            
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    if i != j and i != k and j != k:
                            if li[i] + li[j] + li[k] == tg:
                                temp = sorted([li[i], li[j], li[k]])
                                if temp not in result:
                                    result.append(temp)
        return result

    def three_sum_while(self, li, tg):
        li.sort()
        length = len(li) 
        result = []

        for i in range(length - 2):
            if i > 0 and li[i] == li[i - 1]:
                continue
            
            left = i + 1
            right = length - 1

            while (left < right):
                sum = li[i] + li[left] + li[right]

                if sum < tg:
                    left += 1
                elif sum > tg:
                    right -= 1
                else:
                    result.append([li[i], li[left], li[right]])
                    while left > length - 1 and li[left] == li[left + 1]:
                        left += 1
                    while right > 0 and li[right] == li[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

    """ 4SUM """
    def four_sum_nested(self, li, tg):
        li.sort()
        result = []
        length = len(li)
    
        for i in range(length):
            for j in range(length):
                for k in range(length):
                    for l in range(length):
                        if i != j and i != k and i != l and j != k and j != l and k != l:
                            if li[i] + li[j] + li[k] + li[l] == tg:
                                temp = sorted([li[i], li[j], li[k], li[l]])
                                if temp not in result:
                                    result.append(temp)
        return result

    def four_sum_while(self, li, tg):
        li.sort()
        length = len(li) 
        result = []

        for x in range(length - 3):
            if x > 0 and li[x] == li[x - 1]:
                    continue
                
            for i in range(1, length - 2):
                left = i + 1
                right = length - 1
    
                while left < right:
                    sum = li[i] + li[left] + li[right]
    
                    if sum < tg - li[x]:
                        left += 1
                    elif sum > tg - li[x]:
                        right -= 1
                    else:
                        if (x != i) and (x != left) and (x != right):
                            temp = sorted([li[x], li[i], li[left], li[right]])
                            if temp not in result:
                                result.append(temp)
                        while left > length - 1 and li[left] == li[left + 1]:
                            left += 1
                        while right > 0 and li[right] == li[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result


sums = [
    { "nums": [], "target": 6 },
    { "nums": [3], "target": 6 },
    { "nums": [3, 3, 3, 3, 3, 3], "target": 3 },
    { "nums": [0, 1, 3, 4, 5, 6, 7, 8, 9], "target": 9 },
    { "nums": [0, 1, 3, 4, 5, 6, 7, 8, 9, 0, 9], "target": 9 },
    { "nums": [9, 0, 3, 3, 3, 4, 5, 9], "target": 9 },
    { "nums": [1, 1, 1, 1], "target": 2 },
    { "nums": [1, 2, 3], "target": 3 },
    { "nums": [3, -3, 0, -6, 3, 3, 3], "target": 6 },
    { "nums": [-1, 0, 1, 2, -1, -4], "target": 0 },
    { "nums": [2, 7, 4, 0, 9, 5, 1, 3], "target": 20 },
    { "nums": [1, 0, -1, 0, -2, 2], "target": 0 },
    { "nums": [2, 2, 2, 2, 2], "target": 8 },
]


solution = Solution(sums)
print(solution.result)
