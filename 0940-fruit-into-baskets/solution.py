class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        start = 0
        max_fruits = 0

        fruit_type = defaultdict(int)

        for end in range(len(fruits)):

            fruit_type[fruits[end]] += 1

            while len(fruit_type) > 2:

                fruit_type[fruits[start]] -= 1

                if fruit_type[fruits[start]] == 0:
                    del fruit_type[fruits[start]]
                start+=1

            max_fruits = max(max_fruits, end - start+1)

        return max_fruits

            
        
