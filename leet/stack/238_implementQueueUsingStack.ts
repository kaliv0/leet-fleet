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

const myQueueCases = [
    {
        steps: [
            { op: "push", x: 1 },
            { op: "push", x: 2 },
            { op: "peek", result: 1 },
            { op: "pop", result: 1 },
            { op: "empty", result: false },
        ],
    },
];

myQueueCases.forEach(({ steps }) => {
    const queue = new MyQueue();
    steps.forEach((step) => {
        if (step.op === "push") {
            queue.push(step.x!);
        } else if (step.op === "peek") {
            const actual = queue.peek();
            console.assert(actual === step.result, `${actual} !== ${step.result}`);
        } else if (step.op === "pop") {
            const actual = queue.pop();
            console.assert(actual === step.result, `${actual} !== ${step.result}`);
        } else if (step.op === "empty") {
            const actual = queue.empty();
            console.assert(actual === step.result, `${actual} !== ${step.result}`);
        }
    });
});
