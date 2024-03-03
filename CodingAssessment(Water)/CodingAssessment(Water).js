function calculateFillTime(queue, numTaps) {
    let totalTime = 0;
    while (queue.length > 0) {
        for (let i = 0; i < Math.min(numTaps, queue.length); i++) {
            let bottleSize = queue.shift();
            let fillTime = bottleSize / 100;
            totalTime += fillTime;
        }
    }
    return totalTime;
}

let queue = [400, 750, 1000];
let numTaps = 2;
console.log("Total time required:", calculateFillTime(queue, numTaps), "seconds");


function calculateFillTimeWithInputValidation(queue, numTaps) {
    if (!Array.isArray(queue) || !queue.every(x => typeof x === "number")) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (typeof numTaps !== "number" || numTaps <= 0) {
        throw new Error("Number of taps must be a positive integer.");
    }
    
    let totalTime = 0;
    while (queue.length > 0) {
        for (let i = 0; i < Math.min(numTaps, queue.length); i++) {
            let bottleSize = queue.shift();
            let fillTime = bottleSize / 100;
            totalTime += fillTime;
        }
    }
    return totalTime;
}

queue = [400, 750, 1000];
numTaps = 1;
console.log("Total time required:", calculateFillTimeWithInputValidation(queue, numTaps), "seconds");


function calculateFillTimeWithWalkingTime(queue, numTaps, walkingTimePerPerson) {
    if (!Array.isArray(queue) || !queue.every(x => typeof x === "number")) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (typeof numTaps !== "number" || numTaps <= 0) {
        throw new Error("Number of taps must be a positive integer.");
    }
    if (typeof walkingTimePerPerson !== "number" || walkingTimePerPerson < 0) {
        throw new Error("Walking time per person must be a non-negative number.");
    }
    
    let totalTime = 0;
    while (queue.length > 0) {
        totalTime += walkingTimePerPerson * Math.min(numTaps, queue.length);
        for (let i = 0; i < Math.min(numTaps, queue.length); i++) {
            let bottleSize = queue.shift();
            let fillTime = bottleSize / 100;
            totalTime += fillTime;
        }
    }
    return totalTime;
}

queue = [400, 750, 1000];
numTaps = 3;
let walkingTimePerPerson = 2; 
console.log("Total time required:", calculateFillTimeWithWalkingTime(queue, numTaps, walkingTimePerPerson), "seconds");


function calculateFillTimeWithFlowRates(queue, tapFlowRates, walkingTimePerPerson) {
    if (!Array.isArray(queue) || !queue.every(x => typeof x === "number")) {
        throw new TypeError("Queue must be an array of integers.");
    }
    if (!Array.isArray(tapFlowRates) || !tapFlowRates.every(rate => typeof rate === "number")) {
        throw new TypeError("Tap flow rates must be an array of numbers.");
    }
    if (tapFlowRates.some(rate => rate <= 0)) {
        throw new Error("Tap flow rates must be positive.");
    }
    if (typeof walkingTimePerPerson !== "number" || walkingTimePerPerson < 0) {
        throw new Error("Walking time per person must be a non-negative number.");
    }
    
    let totalTime = 0;
    while (queue.length > 0) {
        totalTime += walkingTimePerPerson * queue.length;
        let fastestTapIndex = tapFlowRates.indexOf(Math.max(...tapFlowRates));
        let fillTime = queue.shift() / tapFlowRates[fastestTapIndex];
        totalTime += fillTime;
    }
    return totalTime;
}

queue = [400, 750, 1000];
let tapFlowRates = [50, 200];
walkingTimePerPerson = 2;
console.log("Total time required:", calculateFillTimeWithFlowRates(queue, tapFlowRates, walkingTimePerPerson), "seconds");


function calculateFillTimeAndFlowRateWithFlowRates(queue, tapFlowRates, walkingTimePerPerson) {
    if (!Array.isArray(queue) || !queue.every(x => typeof x === 'number')) {
        throw new TypeError("Queue must be an array of numbers.");
    }
    if (!Array.isArray(tapFlowRates) || !tapFlowRates.every(rate => typeof rate === 'number')) {
        throw new TypeError("Tap flow rates must be an array of numbers.");
    }
    if (tapFlowRates.some(rate => rate <= 0)) {
        throw new ValueError("Tap flow rates must be positive.");
    }
    if (typeof walkingTimePerPerson !== 'number' || walkingTimePerPerson < 0) {
        throw new ValueError("Walking time per person must be a non-negative number.");
    }

    let totalTime = 0;
    let fastestTapIndex = 0;
    while (queue.length > 0) {
        totalTime += walkingTimePerPerson * queue.length;
        fastestTapIndex = tapFlowRates.indexOf(Math.max(...tapFlowRates));
        let fillTime = queue.shift() / tapFlowRates[fastestTapIndex];
        totalTime += fillTime;
    }
    return [totalTime, tapFlowRates[fastestTapIndex]];
}

queue = [400, 750, 1000];
tapFlowRates = [50, 200];
walkingTimePerPerson = 2;
let [totalTime, usedFlowRate] = calculateFillTimeAndFlowRateWithFlowRates(queue, tapFlowRates, walkingTimePerPerson);
console.log("Total time required:", totalTime, "seconds");
console.log("Flow rate of the tap used:", usedFlowRate, "ml/s");

