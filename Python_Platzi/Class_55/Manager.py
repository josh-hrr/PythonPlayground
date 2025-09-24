'''
When processes must share complex data structures (such as lists or dictionaries), we can use a **Manager** to create a shared memory space between processes.

'''

import multiprocessing

def add_values(shared_list):
    for i in range(5):
        shared_list.append(i)

if __name__ == "__main__":
    with multiprocessing.Manager() as manager:
        shared_list = manager.list()

        process1 = multiprocessing.Process(target=add_values, args=(shared_list,))
        process2 = multiprocessing.Process(target=add_values, args=(shared_list,))

        process1.start()
        process2.start()

        process1.join()
        process2.join()

        print(f"Shared list: {shared_list}")