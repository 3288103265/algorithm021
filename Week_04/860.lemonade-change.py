class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        pocket = defaultdict(int)
        for bill in bills:
            if bill == 5:
                pocket[bill] += 1
            if bill == 10:
                if pocket[5] > 0:
                    pocket[5] -= 1
                    pocket[bill] += 1
                else:
                    return False
            if bill == 20:
                if pocket[10] >=1 and pocket[5] >=1: #优先找10 + 5
                    pocket[10] -= 1
                    pocket[5] -= 1
                    pocket[bill] += 1
                elif pocket[5] >=3: # 找5*3
                    pocket[5] -= 3
                    pocket[bill] += 1
                else:
                    return False
        
        return True
