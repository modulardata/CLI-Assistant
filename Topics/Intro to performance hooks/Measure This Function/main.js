const { performance } = require('perf_hooks');

let start = performance.now();
toMeasure().then(() => {
  let end = performance.now();
  let executionTime = end - start;
  console.log(executionTime);
});
