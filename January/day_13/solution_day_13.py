class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats, low, high = 0, 0, len(people) - 1
        while low <= high:
            boats += 1
            if people[low] + people[high] <= limit:
                low += 1
            high -= 1
        return boats
