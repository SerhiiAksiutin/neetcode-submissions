class MinStack {

    public Stack<Integer> mainStack;
    public Stack<Integer> sideStack;

    public MinStack() {
        this.mainStack = new Stack<>();
        this.sideStack = new Stack<>();
    }
    
    public void push(int val) {
        if (this.mainStack.isEmpty()) {
            this.sideStack.push(val);
        } else {
            if (this.sideStack.peek() >= val) {
                this.sideStack.push(val);
            }
        }
        this.mainStack.push(val);
    }
    
    public void pop() {
        int val = this.mainStack.pop();
        if (this.sideStack.peek() == val) {
            this.sideStack.pop();
        }
    }
    
    public int top() {
        return this.mainStack.peek();
    }
    
    public int getMin() {
        return this.sideStack.peek();
    }
}
