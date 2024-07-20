import socket, os, time, requests, time, secrets, random, sys, json, platform

class config:
    VERSION = "1.0.0"
    AUTHOR = "harimtim"
    DOCUMENTION = "https://github.com/harimtim/EZPY"

def showconfig() -> str:
    try:
        output = f"VERSION: {config.VERSION}\nAUTHOR: {config.AUTHOR}\nDOCUMENTATION: {config.DOCUMENTION}"
        return output
    except:
        pass

def clear() -> None:
    try:
        os.system("cls")
    except:
        try:
            os.system("clear")
        except:
            pass


def mytime() -> str:
    try:
        return time.strftime("%d.%m.%y : %T")
    except:
        raise


def justtime() -> str:
    try:
        return time.strftime("%T")
    except:
        raise


def load_json(json_file_path) -> None:
    with open(json_file_path, "r") as file:
        return json.load(file)


def save_json(data, json_file_path) -> None:
    with open(json_file_path, "w") as file:
        json.dump(data, file, indent=4)


def myinfo() -> dict:
    try:
        info = {}
        info["OS"] = platform.system()
        info["Version"] = platform.version()
        info["Structure"] = platform.machine()
        return info
    except:
        pass
    

def start_timer() -> None:
    try:
        return time.time()
    except:
        pass

def get_timer(timer: int) -> None:
    try:
        return f"{round(time.time() - timer, 2)}"
    except:
        pass
