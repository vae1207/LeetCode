def hasCycle(self,head):
  
  
  list_id = []
  while head:
    if id(head) in list_id:
        return True
    list_id.append(id(head))
    head = head.next
  return False
