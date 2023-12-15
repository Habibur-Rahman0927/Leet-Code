class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        cities = set()

        # Collect outgoing cities
        for path in paths:
            cities.add(path[0])

        # Find destination city with no outgoing path
        for path in paths:
            dest = path[1]
            if dest not in cities:
                return dest

        return ""