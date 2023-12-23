
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        content_map = defaultdict(list)

        for directory in paths:
            items = directory.split(" ")
            parent_path = items[0]

            for file_content in items[1:]:
                file_name, content = file_content.split("(")
                content_map[content].append("{}/{}".format(parent_path, file_name))
                

        return [paths for content, paths in content_map.items() if len(paths) > 1]