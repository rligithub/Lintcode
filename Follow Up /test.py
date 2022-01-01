class Solution():
    def minSession(self, tasks, sessiontime):
        if not tasks or not sessiontime:
            return 0

        start, end = sessiontime // sum(tasks), len(tasks)
        if sum(tasks) <= sessiontime:
            return 1
        while start +1 < end:
            mid = start + (end - start)//2
            if self.eachsectiontime(tasks, mid) > sessiontime:
                start = mid
            else:
                end = mid
        if self.eachsectiontime(tasks, start) <= sessiontime:
            return start
        if self.eachsectiontime(tasks, end) <= sessiontime:
            return end


    def eachsectiontime(self, tasks, k):
        if not tasks:
            return 0
        start, end = max(tasks), sum(tasks)
        while start + 1 < end:
            mid = (end - start) // 2 + start
            if self.sectionneed(tasks, mid) > k:
                start = mid
            else:
                end = mid
        if self.sectionneed(tasks, start) <= k:
            return start
        if self.sectionneed(tasks, end) <= k:
            return end


    def sectionneed(self, tasks, time):
        sum = 0
        count = 0
        for task in tasks:
            if sum + task > time:
                count += 1
                sum = 0
            sum += task
        return count + 1






tasks = [9,8,8,4,6]
time = 14

a= Solution()
print(a.minSession(tasks,time))