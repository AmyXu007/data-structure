# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    import heapq
    result = [AssignedJob(-1,-1)]*len(jobs)
    # initialize a min-heap size n
    # cell in the heap as (end_time, thread, )
    minheap = []
    if n_workers > len(jobs):
        n_workers = len(jobs)
    for i in range(n_workers):
        minheap.append((jobs[i], i))
        result[i] = AssignedJob(i, 0)
    heapq.heapify(minheap)
    for i in range(n_workers, len(jobs)):
        finish_time, finish_thread = heapq.heappop(minheap)
        result[i] = AssignedJob(finish_thread, finish_time)
        heapq.heappush(minheap, (jobs[i]+finish_time, finish_thread))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
