class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        toTouple = list(zip(position,speed))
        print(toTouple)
        sortedPosition = sorted(toTouple, key=lambda x: x[0], reverse=True)
        print(sortedPosition)
        stack = [0]
        for car in sortedPosition:
            time = ((target - car[0]) / car[1])
            if time <= stack[-1] or car[1] == 0:
                continue
            stack.append(time)
        return (len(stack) - 1)


