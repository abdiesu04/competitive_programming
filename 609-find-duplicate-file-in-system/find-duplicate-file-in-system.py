class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        Map=defaultdict(list)
        for path in paths:
           path= path.split()
           root=path[0]
           for i in path[1:]:
               txt,_,content=i.partition('(')
               Map[content].append(root+'/'+txt)
        return[x for x in Map.values() if len(x)>1]



       
        