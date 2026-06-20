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
        this.head = null;
        this.tail = null;
    }

    public boolean isEmpty() {
        return head == null && tail == null;
    }

    public void append(int value) {
        ListNode newNode = new ListNode(value);
        if (head == null) {
            head = newNode;
        } else if (tail != null) {
            tail.next = newNode;
            newNode.prev = tail;
        }
        tail = newNode;
    }

    public void appendleft(int value) {
        ListNode newNode = new ListNode(value);
        if (tail == null) {
            tail = newNode;
        } else if (head != null) {
            head.prev = newNode;
            newNode.next = head;
        }
        head = newNode;
    }

    public int pop() {
        if (head == null && tail == null) {
            return -1;
        }
        int value = tail.val;
        if (tail.prev == null) {
            head = null;
            tail = null;
        } else {
            tail = tail.prev;
            tail.next = null;
        }
        return value;
    }

    public int popleft() {
        if (head == null && tail == null) {
            return -1;
        }
        int value = head.val;
        if (head.next == null) {
            head = null;
            tail = null;
        } else {
            head = head.next;
            head.prev = null;
        }
        return value;
    }
}
