# OurPy

The best module when you like to keep your code simple and clean!
OurPy ist ein Python-Modul, das verschiedene Dienstprogramme für Konfigurationsmanagement, Threading, Systeminformationen, JSON-Dateiverarbeitung und Netzwerkoperationen bereitstellt.

## Funktionen

- **Konfigurationsmanagement:** Einfacher Zugriff auf Modulversion, Autor und Dokumentations-URL.
- **Threading:** Ausführen von Jobs in separaten Threads.
- **Systemoperationen:** Konsole löschen, Verzögerungen verwalten und aktuelle Zeit abrufen.
- **JSON-Verarbeitung:** Laden und Speichern von JSON-Daten.
- **Systeminformationen:** Abrufen von Betriebssystem-, Versions- und Architekturdetails.
- **Timing:** Starten und Abrufen von Timern für Leistungsbewertungen.
- **Netzwerkoperationen:** Entdecken von Online-Geräten im lokalen Netzwerk und Auflösen von Hostnamen.

## Installation

Install the PyPi module locally on your PC:

```py
pip install ourpy
```

## Usage 

```py

from ourpy import *

# Clear Terminal

clear()


# Terminal Colors

print(f"{COLORS.RED} RED Text")
print(f"{COLORS.GREEN} GREEN Text")
print(f"{COLORS.BLUE} BLUE Text")
print(f"{COLORS.WHITE} WHITE Text")
print(f"{COLORS.CYAN} CYAN Text")


# Wait X seconds | Delay(x: int)

delay(x)


# Track operation timing in your code

start_time = start_timer()
"FOR EXAMPLE | YOUR CODE HERE"
duration_of_operation = get_timer(start_time)
print(duration_of_operation)


# Windows PATHS

desktop_path = PATHS.desktop
startup_folder = PATHS.startup
temp_folder = PATHS.temp


# Start function in thread

def job():
    while True:
        print("Hello World!")
        delay(1)

start_in_thread(job)
print("Job started!")


# System Information

print(myinfo())
"OUTPUT EXAMPLE: {'OS': 'Windows', 'Version': '23.3452.12', 'Structure': 'AMD64'}"


# Local Time

print(mytime())
"OUTPUT EXAMPLE: 10.10.2000 : 12:45:34"
print(justtime())
"OUTPUT EXAMPLE: 12:45:34"


# JSON Handling

data = {"KEY": "VALUE"}
save_json(data, "file.json")

loaded_data = load_json(data)
loaded_data["KEY"] = "VALUE2"
save_json(loaded_data, "file.json")


# Online Devices in Local Network with IP

online_devices = get_online_devices_local()
print(online_devices)


# Animate text to terminal

animate_text("Hello World!", 0.09)


# Text into Ascii art

print(into_art("OurPy"))
```