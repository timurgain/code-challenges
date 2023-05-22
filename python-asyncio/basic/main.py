import asyncio
import api

async def sent_data(to_user: str):
    print(f"Sending data to {to_user}")
    await asyncio.sleep(2)
    print(f'Data sent to {to_user}')

async def kill_time(num: int):
    print('Running: ', num)
    await asyncio.sleep(1)
    print('Finished: ', num)

async def main():
    # 1. basic execute task
    data = await api.fetch_data()
    print('Data: ', data)
    await sent_data('Lea')

    # 2. create and cancel scheduled task
    task = asyncio.create_task(
        api.fetch_data()
    )
    # await asyncio.sleep(3)

    # 2.1. tasks canceling
    # task.cancel()
    # await asyncio.sleep(1)
    # if task.cancelled():
    #     print(task.cancelled())

    try:
        # 2.2. check if done
        if task.done():
            print(task.result())

        # 2.3 set up a time limit
        await asyncio.wait_for(task, timeout=1)

        result = await task
        print(result)
    except asyncio.CancelledError:
        print('Error: scheduled request was cancelled')
    except asyncio.TimeoutError:
        print('Error: scheduled request took too long')

    # 3. execute list of tasks
    another_list_of_tasks = [kill_time(i) for i in range(1, 11)]
    await asyncio.sleep(2)
    await asyncio.gather(*another_list_of_tasks, sent_data('Luke'))
    print('Done')


if __name__ == '__main__':

    asyncio.run(main())
