import psutil

def check_system_health():
    cpu_threshold=int(input("Enter the cpu threshold value(in percents): "))
    disk_threshold=int(input("Enter the disk threshold value(in percents): "))
    memory_threshold=int(input("Enter the memory threshold value(in percents): "))

    cpu_usage=psutil.cpu_percent(interval=1)
    print(f"Current cpu usage is: {cpu_usage}%")
    disk_usage=psutil.disk_usage('/').percent
    print(f"Current disk usage is: {disk_usage}%")
    memory_usage=psutil.virtual_memory().percent
    print(f"Current memory usage is: {memory_usage}%")

    if cpu_usage > cpu_threshold:
        print("CPU alert")
    else:
        print("CPU running safely")

    if disk_usage > disk_threshold:
        print("disk alert")
    else:
        print("you can use the disk safely")
    
    if memory_usage > memory_threshold:
        print("memory alert")
    else:
        print("you can use the memory safely")


if __name__ == "__main__":
    check_system_health()