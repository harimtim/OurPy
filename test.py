import ourpy

data = {"Server": {"Version": "1.0"}}


def job():
    x = 0
    while x < 10:
        print(x)
        ourpy.delay(1)


ourpy.clear()

print(ourpy.showconfig())

print(ourpy.myinfo())

timer = ourpy.start_timer()

ourpy.delay(3.34)

print(str(ourpy.get_timer(timer)).replace(".", ","), "Seconds")

ourpy.save_json(data, "test.json")

my_data = ourpy.load_json("test.json")

my_data["Server"]["Version"] = "1.1"
my_data["Server"]["Message"] = "Hello from Ourpy!"

ourpy.save_json(my_data, "test.json")

ourpy.start_in_thread(job=job)

print(ourpy.mytime())
print(ourpy.justtime())
print(ourpy.get_online_devices_local())