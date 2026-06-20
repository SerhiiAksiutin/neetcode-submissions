class DynamicArray {
    
    public int[] arr;
    public int capacity;
    public int length;

    public DynamicArray(int capacity) {
        this.arr = new int[capacity];
        this.length = 0;
        this.capacity = capacity;
    }

    public int get(int i) {
        return this.arr[i];
    }

    public void set(int i, int n) {
        this.arr[i] = n;
    }

    public void pushback(int n) {
        if (this.length >= this.capacity) {
            this.resize();
        }
        this.arr[this.length] = n;
        this.length++;
    }

    public int popback() {
        int popValue = this.arr[this.length - 1];
        this.length--;
        return popValue;
    }

    private void resize() {
        this.capacity = 2 * this.capacity;
        int[] newArr = new int[this.capacity];
        for (int i = 0; i < this.length; i++) {
            newArr[i] = this.arr[i];
        }
        this.arr = newArr;
    }

    public int getSize() {
        return this.length;
    }

    public int getCapacity() {
        return this.capacity;
    }
}
