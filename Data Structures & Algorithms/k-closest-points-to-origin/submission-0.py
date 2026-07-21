class Solution:
    def sort(self, lst, s, e):
        p1 = s 
        p2 = e
        if s >= e: 
            return 

        pivot = lst[e]
        #partition: elements smaller than pivot on left side
        for i in range(s,e):
            if lst[i] < pivot:
                tmp = lst[s]
                lst[s] = lst[i]
                lst[i] = tmp
                s += 1
        
        # move pivot in-between left and right sides
        lst[e] = lst[s]
        lst[s] = pivot

        self.sort(lst, p1, s - 1)
        self.sort(lst, s + 1, p2)

        return lst

    #calc distance 
    def dist(self, pt):
        return pt[0] ** 2 + pt[1] ** 2
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if len(points) == k:
            return points

        lst = []
        
        for point in points:
            dist = self.dist(point)
            lst.append([dist, point[0], point[1]])

        self.sort(lst, 0, len(lst) - 1)

        res = [item[1:] for item in lst]

        return res[:k]

    

