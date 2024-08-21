CACHING SYSTEM

Caching System
A caching system is a mechanism that stores copies of data or computations so that future requests for that data can be served faster. Instead of repeatedly fetching the data from a slower source (like a database or external service), the cache provides quick access to the cached data, improving performance and reducing latency.

FIFO (First-In, First-Out)
FIFO is a cache eviction policy where the oldest data (the one that was cached first) is removed first when the cache reaches its limit. It's a straightforward method but doesn’t consider the frequency or recency of access.

LIFO (Last-In, First-Out)
LIFO is a cache eviction policy where the most recently added data is removed first when the cache reaches its limit. It’s less common in caching systems because it tends to discard the freshest data, which might still be relevant.

LRU (Least Recently Used)
LRU stands for Least Recently Used. It’s a cache eviction policy that removes the data that hasn’t been accessed for the longest time. This method assumes that data accessed recently will likely be accessed again soon, so it prioritizes keeping such data in the cache.

MRU (Most Recently Used)
MRU stands for Most Recently Used. It’s a cache eviction policy that removes the data that was accessed most recently. This strategy might be used in scenarios where the most recently used data is not likely to be needed again soon.

LFU (Least Frequently Used)
LFU stands for Least Frequently Used. It’s a cache eviction policy that removes the data that is accessed the least frequently. The assumption is that if data is rarely accessed, it’s less likely to be needed in the future, making it a candidate for eviction.

Purpose of a Caching System
The primary purpose of a caching system is to improve performance by reducing the time it takes to access frequently requested data. Caching reduces the load on underlying systems (like databases) by serving data from faster storage, often memory. This leads to faster response times and improved user experience.

Limits of a Caching System
Capacity Limitations: Caches have limited storage, so they can't store all the data. Choosing what to keep and what to evict is a key challenge.

Staleness: Cached data can become outdated if the underlying data changes. This is known as cache staleness.

Complexity: Implementing a caching system and choosing the right eviction policy can be complex, especially when balancing performance with data consistency.

Memory Usage: Caching consumes memory or disk space, and excessive caching can lead to resource exhaustion, affecting the performance of the system.

Overhead: Managing the cache (adding, evicting, updating entries) introduces some overhead, which can offset the performance gains if not managed properly.