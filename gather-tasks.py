import asyncio
from typing import Dict


async def fetch_data(delay: int, id: int) -> Dict[str, int]:
    print(f"Fetching data for id={id}...")
    await asyncio.sleep(delay)
    print(f"Data fetched for id={id}!")
    return {"data": id}


async def main():
    results = await asyncio.gather(
        fetch_data(2, 1),
        fetch_data(1, 2),
        fetch_data(3, 3),
    )

    for result in results:
        print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
