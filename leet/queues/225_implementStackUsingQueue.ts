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

const myStackCases = [
    {
        steps: [
            { op: "push", x: 1 },
            { op: "push", x: 2 },
            { op: "top", result: 2 },
            { op: "pop", result: 2 },
            { op: "empty", result: false },
        ],
    },
];

myStackCases.forEach(({ steps }) => {
    const stack = new MyStack();
    steps.forEach((step) => {
        if (step.op === "push") {
            stack.push(step.x!);
        } else if (step.op === "top") {
            const actual = stack.top();
            console.assert(actual === step.result, `${actual} !== ${step.result}`);
        } else if (step.op === "pop") {
            const actual = stack.pop();
            console.assert(actual === step.result, `${actual} !== ${step.result}`);
        } else if (step.op === "empty") {
            const actual = stack.empty();
            console.assert(actual === step.result, `${actual} !== ${step.result}`);
        }
    });
});
