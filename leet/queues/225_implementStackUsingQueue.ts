//225. Implement Stack using Queues
class MyStack {
    private _queue: number[];

    constructor() {
        this._queue = [];
    }

    push(x: number): void {
        this._queue.push(x);
        // re-arrange all other elemenets to stand behind new one
        for (let i = 0; i < this._queue.length - 1; i++) {
            const elem = this._queue.shift();
            if (elem) {
                this._queue.push(elem);
            }
        }
    }

    pop(): number | undefined {
        return this._queue.shift();
    }

    top(): number {
        return this._queue[0];
    }

    empty(): boolean {
        return !this._queue.length;
    }
}

const myStack = new MyStack();
console.log(myStack.push(1));
console.log(myStack.push(2));
console.log(myStack.top()); // return 2
console.log(myStack.pop()); // return 2
console.log(myStack.empty()); // return False
