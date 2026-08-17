class Solution {
    public ListNode insertionSortList(ListNode head) {
        if(head == null || head.next == null) {
            return head;
        }
        head.next = insertionSortList(head.next);
        return swapIfLarge(head);
    }

    public ListNode swapIfLarge(ListNode head) {
        if(head.next == null||head.next.val>head.val) {
            return head;
        }
        ListNode temp = head.next;
        head.next = temp.next;
        temp.next = swapIfLarge(head);
        return temp;
    }
}