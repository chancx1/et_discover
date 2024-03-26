import os
import psutil
import requests



def check_server_status():
    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()
    memory_usage = {
        "total": f"{memory.total // (1024**3)} GB",
        "available": f"{memory.available // (1024**3)} GB",
        "used": f"{memory.used // (1024**3)} GB",
        "free": f"{memory.free // (1024**3)} GB"
    }

    disk_partitions = psutil.disk_partitions()
    disk_usage = {}
    for partition in disk_partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_usage[partition.mountpoint] = {
            "total": f"{usage.total // (1024**3)} GB",
            "used": f"{usage.used // (1024**3)} GB",
            "free": f"{usage.free // (1024**3)} GB"
            }

    dire_sec = {
            "web1" : "/var/www/html",
            "user" : "/etc/passwd",
            "pass" : "etc/shadow",
            "tmp"  : "/tmp",
            }


    sql_sec = True


    return {
        "CPU占用状态 (%)": cpu_usage ,
        "内存占用状态 (bytes)": memory_usage,
        "磁盘空间状态": disk_usage,
        "木马检测": dire_sec
    }


#def send_json(data):
#    requests.send


data = check_server_status()


output_str = ""
for key, value in data.items():
    if isinstance(value, dict):
        output_str += f"{key}:\n"
        for sub_key, sub_value in value.items():
            output_str += f"  {sub_key}: {sub_value}\n"
    else:
        output_str += f"{key}: {value}\n"

print(output_str)
