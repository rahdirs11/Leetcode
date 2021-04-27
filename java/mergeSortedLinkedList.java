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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode l3 = null, l3Ptr = null;
        ListNode left = l1, right = l2;
        while (left != null && right != null) {
            ListNode ptr;
            if (left.val <= right.val) {
                ptr = new ListNode(left.val);
                left = left.next;
            } else {
                ptr = new ListNode(right.val);
                right = right.next;
            }
            if (l3 == null) {
                l3 = ptr;
            } else {
                if (l3Ptr == null) {
                    l3Ptr = ptr;
                    l3.next = l3Ptr;
                } else {
                    l3Ptr.next = ptr;
                    l3Ptr = ptr;
                }
            }
        }
        if (right == null)System.out.println("Right is empty");
        
        while (left != null) {
            if (l3 == null) {
                l3 = left;
            } else {
                if (l3Ptr == null) {
                    l3Ptr = left;
                    l3.next = l3Ptr;
                } else {
                    l3Ptr.next = left;
                    l3Ptr = left;
                }
            }
            left = left.next;
        }
        while (right != null) {
            if (l3 == null) {
                l3 = right;
            } else {
                if (l3Ptr == null) {
                    l3Ptr = right;
                    l3.next = l3Ptr;
                } else {
                    l3Ptr.next = right;
                    l3Ptr = right;
                }
            }
            right = right.next;
        }
        return l3;
    }
}