class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        freqs = sorted(counts.values(), reverse=True)

        max_frq = freqs[0]
        idle = (max_frq - 1) * n

        for i in range(1, len(freqs)):
            idle -= min(max_frq - 1, freqs[i])

        idle = max(0, idle)

        return len(tasks) + idle