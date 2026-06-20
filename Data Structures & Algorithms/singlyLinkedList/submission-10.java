class LinkedList {

    public ListNode head;
    public ListNode tail;

    public LinkedList() { }

    public int get(int index) {
        ListNode cur = head;
        int i = 0;
        while (i < index && cur != null) {
            i++;
            cur = cur.next;
        }
        return cur == null ? -1 : cur.val;
    }

    public void insertHead(int val) {
        ListNode newHead = new ListNode(val);
        if (head == null) {
            tail = newHead;
        } else {
            newHead.next = head;
        }
        head = newHead;
    }

    public void insertTail(int val) {
        ListNode newTail = new ListNode(val);
        if (tail == null) {
            head = newTail;
        } else {
            tail.next = newTail;
        }
        tail = newTail;
        System.out.println(head);
        System.out.println(this.getValues());
    }

    public boolean remove(int index) {
        if (index == 0) {
            if (head == null) {
                return false;
            }
            head = head.next;
            return true;
        }
        ListNode prev = null;
        ListNode cur = head;
        int i = 0;
        while (i < index && cur != null) {
            i++;
            prev = cur;
            cur = cur.next;
        }
        if (cur == null) {
            return false;
        }
        if (cur.next == null) {
            tail = prev;
        }
        prev.next = cur.next;
        return true;
    }

    public ArrayList<Integer> getValues() {
        ListNode cur = head;
        ArrayList<Integer> list = new ArrayList<>();
        while (cur != null) {
            list.add(cur.val);
            cur = cur.next;
        }
        return list;
    }
}

class ListNode {

    public int val;
    public ListNode next;

    public ListNode() { }

    public ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    public ListNode(int val) {
        this.val = val;
    }

}