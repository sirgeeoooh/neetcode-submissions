class Node:
    def __init__(self, url=None, previous=None, forward=None):
        self.url = url
        self.previous = previous
        self.forward = forward


class BrowserHistory:
    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.current = self.head

    def visit(self, url: str) -> None:
        previous = self.current
        node = Node(url)
        previous.forward = node
        self.current = node
        self.current.previous = previous


    def back(self, steps: int) -> str:
        current = self.current
        while current.previous and steps > 0:
            current = current.previous
            steps -= 1
        self.current = current
        return current.url

    def forward(self, steps: int) -> str:
        current = self.current
        while current.forward and steps > 0:
            current = current.forward
            steps -= 1
        self.current = current
        return current.url