from collections import defaultdict
from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapp = defaultdict(int)
        for i in cpdomains:
            visit, d = i.split()
            subdomains = d.split('.')
            for j in range(len(subdomains)):
                domain = '.'.join(subdomains[j:])
                mapp[domain] += int(visit)
        res = []
        for key, value in mapp.items():
            res.append(str(value) + " " + key)
        return res