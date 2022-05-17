from SingularSpaceSolution import MinStackSpaceConstraint


# Your MinStack object will be instantiated and called as such:
obj = MinStackSpaceConstraint()
obj.push(18)
obj.push(19)
obj.push(29)
obj.push(15)
obj.push(16)
print(obj.top())
print(obj.getMin())
obj.pop()
obj.pop()
print(obj.top())
print(obj.getMin())
