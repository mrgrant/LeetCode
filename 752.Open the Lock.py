class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if "0000" in deadends:
            return -1
        q1 = set()
        q2 = set()
        q1.add("0000")
        q2.add("target")
        step = 0
        visited = set(deadends)
        while q1 and q2:
            temp = set()
            for lock in q1:
                if lock in visited:
                    continue
                if lock in q2:
                    return step
                visited.add(lock)
                for i in range(4):
                    newLock1 = lock[:i] + str((int(lock[i]) + 1) % 10) + lock[i+1:]
                    if newLock1 not in visited:
                        temp.add(newLock1)
                    newLock2 = lock[:i] + str((int(lock[i]) - 1) % 10) + lock[i+1:]
                    if newLock2 not in visited:
                        temp.add(newLock2)
            q1 = q2
            q2 = temp
            step += 1
        return -1

if __name__ == "__main__":
    obj = Solution()
    deadends = ["0201","0101","0102","1212","2002"]
    target = "0202"
    obj.openLock(deadends, target)