/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists.length <= 1 || lists[0] == null) {
            return null;
        }
        for (int i = 1; i < lists.length; i++) {
            lists[i] = mergeTwoLists(lists[i - 1], lists[i]);
        }
        return lists[lists.length - 1];
    }

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode cur1 = list1;
        ListNode cur2 = list2;
        ListNode res = new ListNode(0);
        ListNode head = res;
        while (cur1 != null && cur2 != null) {
            if (cur1.val <= cur2.val) {
                res.next = cur1;
                cur1 = cur1.next;
            } else {
                res.next = cur2;
                cur2 = cur2.next;
            }
            res = res.next;
        }

        if (cur1 != null) {
            res.next = cur1;
        } else if (cur2 != null) {
            res.next = cur2;
        }

        return head.next;
    }
}
