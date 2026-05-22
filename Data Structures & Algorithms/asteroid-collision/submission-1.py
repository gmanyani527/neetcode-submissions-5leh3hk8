class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        abs value of each asteroid == size 
        positive means moving right
        negative means moving left
        asteroids all move at the same speed

        when two asteroids meet:
        small one explodes
        if both equal same size both explode
        two move in same direction will never meet

        '''

        stack = []

        for asteroid in asteroids: 
            alive = True
            while alive and stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    alive = False
                else: 
                    alive = False
            if alive:
                stack.append(asteroid)
        return stack