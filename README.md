# Simple Python TCP Banner Grabber 

A lightweight Python script created to understand network socket programming and banner grabbing basics. This tool connects to a specified target IP address and port to retrieve the initial welcome message (banner) exposed by the service.

---

##  How It Works

1. **Establishes a Socket Connection:** Creates an `AF_INET` (IPv4) `SOCK_STREAM` (TCP) socket.
2. **Connects to Target:** Connects to the defined IP address and port (e.g., `127.0.0.1:8080`).
3. **Receives Banner:** Listens for incoming bytes up to `1024` bytes.
4. **Decodes & Displays:** Decodes the binary response using `UTF-8` encoding and prints the service banner to the console.

---

##  Prerequisites

* Python 3.x installed on your machine.
* A listening service or netcat listener to test against (e.g., `nc -lvp 8080`).

---

