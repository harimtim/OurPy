import ourpy
import time

data = {
    "Server": {
        "Version": "1.0"
    }
}

ourpy.clear()
print(ourpy.showconfig())
print(ourpy.myinfo())
timer = ourpy.start_timer()
time.sleep(3.34)
print(str(ourpy.get_timer(timer)).replace(".", ","), "Seconds")
ourpy.save_json(data, "test.json")
my_data = ourpy.load_json("test.json")
my_data["Server"]["Version"] = "1.1"
my_data["Server"]["Message"] = "Hello from Ourpy!"
ourpy.save_json(my_data, "test.json")
print(ourpy.mytime())
print(ourpy.justtime())