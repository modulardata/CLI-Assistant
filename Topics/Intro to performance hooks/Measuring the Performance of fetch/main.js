const { PerformanceObserver } = require('perf_hooks');

const observer = new PerformanceObserver((list) => {
  const entries = list.getEntriesByName('fetchData');
  entries.forEach((entry) => {
    console.log(entry.duration);
  });
});

observer.observe({ entryTypes: ['measure'], buffered: true });

