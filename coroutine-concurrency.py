import asyncio
from typing import Dict


async def fetch_data(delay: int, id: int) -> Dict[str, int]:
    print(f"Fetching data for id={id}...")
    await asyncio.sleep(delay)
    print(f"Data fetched for id={id}!")
    return {"data": id}


async def main():
    task_one = asyncio.create_task(fetch_data(2, 1))
    task_two = asyncio.create_task(fetch_data(3, 2))
    task_three = asyncio.create_task(fetch_data(1, 3))

    result_one = await task_one
    result_two = await task_two
    result_three = await task_three

    print(f"""
          Result one: {result_one}
          Result two: {result_two}
          Result three: {result_three}
        """)

if __name__ == "__main__":
    asyncio.run(main())
