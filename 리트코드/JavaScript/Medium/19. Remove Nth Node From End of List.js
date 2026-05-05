/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
    let ptr = head;
    let temp = head;
    
    for (let i = 0; i < n; i++) {
        ptr = ptr.next;
    }
    
    if (!ptr) return head.next;
    
    while (ptr.next) {
        ptr = ptr.next;
        temp = temp.next;
    }
    
    temp.next = temp.next.next;
    return head;
};