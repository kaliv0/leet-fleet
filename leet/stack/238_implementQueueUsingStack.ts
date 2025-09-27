//232. Implement Queue using Stacks
class MyQueue {
    private _stack1: number[]; // used for pushing new elements
    private _stack2: number[]; // used for popping

    constructor() {
        this._stack1 = [];
        this._stack2 = [];
    }

    push(x: number): void {
        this._stack1.push(x);
    }

    // it's guaranteed that element will never be undefined
    // I guess I will just 'keep calm and hate TS'
    pop(): number | undefined {
        this.migrateElements();
        return this._stack2.pop();
    }

    peek(): number | undefined {
        this.migrateElements();
        return this._stack2.at(-1);
    }

    empty(): boolean {
        return !this._stack1.length && !this._stack2.length;
    }

    private migrateElements(): void {
        if (!this._stack2.length) {
            while (this._stack1.length) {
                const elem = this._stack1.pop();
                // same attitude
                if (elem) {
                    this._stack2.push(elem);
                }
            }
        }
    }
}

const myQueue = new MyQueue();
console.log(myQueue.push(1)); // queue is: [1]
console.log(myQueue.push(2)); // queue is: [1, 2] (leftmost is front of the queue)
console.log(myQueue.peek()); // return 1
console.log(myQueue.pop()); // return 1, queue is [2]
console.log(myQueue.empty()); // return false
