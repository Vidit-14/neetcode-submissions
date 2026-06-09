class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = list(zip(position, speed))
        cars.sort(reverse = True)
        position, speed = zip(*cars)
        position = list(position)
        speed = list(speed)

        stack = []

        for i in range(len(position)):
            hops = (target - position[i]) / speed[i]
            if stack and hops <= stack[-1]:
                continue
            else:
                stack.append(hops)
        
        return len(stack)

