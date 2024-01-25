class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []
        
        stack = []
        
        for fold in path.split('/'):
            if fold:
                folders.append(fold)
        
        for fold in folders:
            if fold not in ['.', '..']:
                stack.append(fold)
            elif fold == ".." and stack:
                stack.pop()
        
        return '/' + '/'.join(stack)
                