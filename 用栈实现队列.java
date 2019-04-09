class MyQueue {

   
    Stack<Integer> stack = new Stack<Integer>();
    public MyQueue() {
        
    }
    
   
    public void push(int x) {
        stack.push(x);
    }
    
   
    public int pop() {
        Stack<Integer> temp = new Stack<Integer>();
        while(!stack.empty()) {
        	int i=stack.pop();
        	temp.push(i);
        }
        int j=temp.pop();
        while(!temp.empty()) {
        	int i=temp.pop();
        	stack.push(i);
        }
        return j;
    }
    
 
    public int peek() {
        Stack<Integer> temp = new Stack<Integer>();
        while(!stack.empty()) {
        	int i=stack.pop();
        	temp.push(i);
        }
        int j=temp.peek();
        while(!temp.empty()) {
        	int i=temp.pop();
        	stack.push(i);
        }
        return j;
    }
    
   
    public boolean empty() {
         return stack.isEmpty();
    }
}
