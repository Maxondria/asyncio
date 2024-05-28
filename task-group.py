import asyncio
from typing import Dict, List


async def fetch_data(delay: int, id: int) -> Dict[str, int]:
    print(f"Fetching data for id={id}...")
    await asyncio.sleep(delay)
    print(f"Data fetched for id={id}!")
    return {"data": id}


async def main():
    tasks: List[asyncio.Task[Dict[str, int]]] = []

    async with asyncio.TaskGroup() as task_group:
        for id, delay in enumerate([2, 1, 3], start=1):
            task = task_group.create_task(fetch_data(delay, id))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
