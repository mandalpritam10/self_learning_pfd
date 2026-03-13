import psutil
def get_cpu_threshold():
    cpu_threshold=int(input("Enter the CPU threshold: "))

    current_cpu=psutil.cpu_percent(interval=1)
    print(f"Current cpu % is: {current_cpu}")
    if current_cpu > cpu_threshold:
        print("CPU Alert Email sent.....")
    else:
        print("CPU is running safely")

get_cpu_threshold()