class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        results= []
        products.sort()

        for i in range(1,len(searchWord)+1):

            temp = [j for j in products if j[0:i] == searchWord[0:i]]

            results.append(temp[:3])
         

        return results
