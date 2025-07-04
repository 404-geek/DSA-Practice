class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        cnt_domains = defaultdict(int)

        res = []

        for d in cpdomains:

            num, domain = d.split(" ")

            cnt_domains[domain]+=int(num)

            domain_subs = domain.split(".")

            n = len(domain_subs)

            i = 1

            while i < n:

                cnt_domains[".".join(domain_subs[i:])]+=int(num)

                i+=1
                


        for k in cnt_domains:

            res.append(f"{cnt_domains[k]} {k}")


        return res




        
