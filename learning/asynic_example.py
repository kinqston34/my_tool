import asyncio
import time
# ex1
# async def main():
#     print("Hello")
#     await asyncio.sleep(1)
#     print("world")

# coro = main()

# asyncio.run(coro)

#============================================================
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     print(what)

# async def main():
#     print(f"started at {time.strftime('%X')}")
#     await say_after(1,"hello")
    
#     await say_after(2,"world")
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())    
#============================================================
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     return f"{what} - {delay}"

# async def main():

#     task1 = asyncio.create_task(say_after(1,"hello"))
#     task2 = asyncio.create_task(say_after(2,"world"))
#     print(f"started at {time.strftime('%X')}")
#     ret1 = await task1
#     ret2 = await task2

#     print("task1 return:",ret1)
#     print("task2 return:",ret2)
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())    
#============================================================
# async def say_after(delay,what):
#     await asyncio.sleep(delay)
#     return f"{what} - {delay}"

# async def main():

#     task1 = asyncio.create_task(say_after(1,"hello"))
#     task2 = asyncio.create_task(say_after(2,"world"))
#     print(f"started at {time.strftime('%X')}")
#     ret = await asyncio.gather(task1,task2)

#     print("task return:",ret)
    
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())    

#============================================================

async def say_after(delay,what):
    await asyncio.sleep(delay)
    return f"{what} - {delay}"

async def main():

    print(f"started at {time.strftime('%X')}")
    ret = await asyncio.gather(say_after(1,"hello"),say_after(2,"world"))

    print("task return:",ret)
    
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())    

