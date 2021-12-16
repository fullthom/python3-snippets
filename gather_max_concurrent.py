from asyncio import coroutine, gather, run, Semaphore, sleep
import random

async def gather_with_concurrency(
    n: int,
    *tasks
) -> coroutine:
    semaphore = Semaphore(n)
    
    async def sem_task(task):
        async with semaphore:
            return await task

    return await gather(*(sem_task(task) for task in tasks))


async def print_it(n, x):
    to_sleep = random.randint(0, x)
    print("{} sleeping for {}".format(n, to_sleep))
    await sleep(to_sleep)
    print("{} finished".format(n))
    return n


async def run_it():
    res = await gather_with_concurrency(10, *[print_it(i, 5) for i in range(100)])
    print(res)

run(run_it())
