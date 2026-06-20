class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return
        
        cur = self.root
        while True:
            if cur.key < key:
                if not cur.right:
                    cur.right = newNode
                    return
                cur = cur.right
            elif cur.key > key:
                if not cur.left:
                    cur.left = newNode
                    return
                cur = cur.left
            else:
                cur.val = val
                return


    def get(self, key: int) -> int:
        cur = self.root

        while cur:
            if cur.key < key:
                cur = cur.right
            elif cur.key > key:
                cur = cur.left
            else:
                return cur.val
        
        return -1

    def getMin(self) -> int:
        if not self.root:
            return -1 

        cur = self.root

        while cur.left:
            cur = cur.left
        
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1 

        cur = self.root

        while cur.right:
            cur = cur.right

        return cur.val

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return 

        if root.key < key:
            root.right = self.removeHelper(root.right, key)
        elif root.key > key:
            root.left = self.removeHelper(root.left, key)
        else:
            if not root.left:
                root = root.right
            elif not root.right:
                root = root.left
            else:
                newMinNode = self.getMinNode(root.right)
                root.key = newMinNode.key
                root.val = newMinNode.val
                root.right = self.removeHelper(root.right, newMinNode.key)
        return root

    def getMinNode(self, root: TreeNode) -> TreeNode:
        while root and root.left:
            root = root.left
        return root

    def getInorderKeys(self) -> List[int]:
        return self.getInorderKeysHelper(self.root)

    def getInorderKeysHelper(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.getInorderKeysHelper(root.left) + [root.key] + self.getInorderKeysHelper(root.right)
