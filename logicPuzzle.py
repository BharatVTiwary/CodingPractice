'''
Given a jug that can hold 4 litres and a jub that can hold 7 litres
Write code to find a solution to get XX litres and print out the steps
'''

from collections import deque
class State():
    def __init__(self, jug4=0, jug7=0):
        self.jug4 = jug4
        self.jug7 = jug7
        self.prev = None

    def __eq__(self, diffState):
        return self.jug4==diffState.jug4 and self.jug7==diffState.jug7
    
    def __str__(self):
        return f'jug4={self.jug4},jug7={self.jug7}'
    
    def __hash__(self):
        return hash((self.jug4, self.jug7))
    
    def isSolved(self, target):
        return self.jug4==target or self.jug7==target

    def nextSteps(self):
        # fill
        if self.jug4 < 4:
            yield State(4, self.jug7)
        if self.jug7 < 7:
            yield State(self.jug4, 7)

        #empty
        if self.jug4 > 0:
            yield State(0, self.jug7)
        if self.jug7 > 0:
            yield State(self.jug4, 0)

        # pour
        diff = min(4 - self.jug4, self.jug7)
        if diff > 0:
            yield State(self.jug4 + diff, self.jug7 - diff)
        
        diff = min(7 - self.jug7, self.jug4)
        if diff > 0:
            yield State(self.jug4 - diff, self.jug7 + diff)

def search(target):
    q = deque()
    st = State()
    seen = set()
    q.append(st)
    while q:
        st = q.popleft()
        if st in seen:
            continue
        seen.add(st)

        if st.isSolved(target):
            # print(seen)
            return st
        
        for ns in st.nextSteps():
            ns.prev = st
            q.append(ns)
    return None

if __name__ == "__main__":
    st = search(6)
    stack = deque()

    while st:
        stack.append(st)
        st = st.prev
    
    while stack:
        print(stack.pop())
        



    
 
