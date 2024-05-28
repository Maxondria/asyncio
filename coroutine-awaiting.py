import asyncio
from typing import Dict


async def fetch_data(delay: int, id: int) -> Dict[str, int]:
    print(f"Fetching data for id={id}...")
    await asyncio.sleep(delay)
    print(f"Data fetched for id={id}!")
    return {"data": id}


async def main() -> None:
    task_one = fetch_data(2, 1)
    task_two = fetch_data(2, 2)

    result_one = await task_one
    print(f"Result one: {result_one}")
    result_two = await task_two
    print(f"Result two: {result_two}")


if __name__ == "__main__":
    asyncio.run(main())
