import json

# with open("list.json", 'r') as f:
#     res = json.load(f)
#     f.close()

# print(res, '\n')

# dictio = {"ggg" : 10, "gk" : "gs", "reff_num" : "hi"}

# res.append(dictio)

# try:
#     temp = res[6]
#     print("oh")
# except:
#     print("omg")

# with open("list.json", 'w') as f:
#     json.dump(res, f)
#     f.close()
# print(res)



def add_task(task, num):
    with open("list.json", 'r') as f:
        all_task = json.load(f)
        f.close()
    
    try:
        temp = all_task[num]
        all_task[num] = {"task": f"{task}"}
        all_task.append(temp)
    except:
        taskd = {"task": f"{task}"}
        all_task.append(taskd)


    with open("list.json", 'w') as f:
        json.dump(all_task, f)
        f.close()

    return all_task