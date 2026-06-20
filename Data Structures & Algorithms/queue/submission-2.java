class ListNode {
    public int val;
    public ListNode prev;
    public ListNode next;

    public ListNode(int val) {
        this.val = val;
        this.prev = null;
        this.next = null;
    }
}

class Deque {
    public ListNode head;
    public ListNode tail;

    public Deque() {
        this.head = new ListNode(0);
        this.tail = new ListNode(0);
        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public boolean isEmpty() {
        return head.next == tail;
    }

    public void append(int value) {
        ListNode newNode = new ListNode(value);
        ListNode backNode = tail.prev;
        backNode.next = newNode;
        newNode.prev = backNode;
        newNode.next = tail;
        tail.prev = newNode;
    }

    public void appendleft(int value) {
        ListNode newNode = new ListNode(value);
        ListNode frontNode = head.next;
        frontNode.prev = newNode;
        newNode.next = frontNode;
        newNode.prev = head;
        head.next = newNode;
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        ListNode poppedNode = tail.prev;
        ListNode newEndNode = poppedNode.prev;
        newEndNode.next = tail;
        tail.prev = newEndNode;
        return poppedNode.val;
    }

    public int popleft() {
        if (isEmpty()) {
            return -1;
        }
        ListNode poppedNode = head.next;
        ListNode newHeadNode = poppedNode.next;
        newHeadNode.prev = head;
        head.next = newHeadNode;
        return poppedNode.val;
    }
}
