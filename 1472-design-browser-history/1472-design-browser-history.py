class Node:
    def __init__(self,val=None):
        self.val = val
        self.next = None
        self. prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.curr_page = self.head
        

    def visit(self, url: str) -> None:
        node = Node(url)
        self.curr_page.next = node
        self.curr_page.next.prev = self.curr_page
        self.curr_page = self.curr_page.next

    def back(self, steps: int) -> str:
        count = 0
        while self.curr_page.prev:
            if count == steps:
                return self.curr_page.val
            count+=1
            self.curr_page = self.curr_page.prev
        return self.curr_page.val

    def forward(self, steps: int) -> str:
        count = 0
        while self.curr_page.next:
            if count == steps:
                return self.curr_page.val
            count+=1
            self.curr_page = self.curr_page.next
        return self.curr_page.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)