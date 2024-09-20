
# **Dauth - Wi-Fi Deauther Project**

## **Overview**

**Dauth** is a desktop-based application for controlling an ESP8266 Wi-Fi deauther over a USB connection (using spacehuhn library, all credits goes to SpaceHuhn). Unlike traditional deauthers, which rely on an access point for control, Dauth enhances security by using a USB connection and requiring a password to unlock its functionality. The Python-based Tkinter GUI allows you to scan for Wi-Fi networks, select specific SSIDs, and perform deauthentication attacks after verifying the correct password.

**Note**: This tool is meant for educational purposes only. It should only be used in a legal and ethical manner. Deauth attacks can disrupt Wi-Fi communications and are illegal in many regions.

## **Features**

- **Password Protection**: The deauther will only activate after receiving the correct password, which adds an additional layer of security.
- **USB-Based Control**: All communication with the ESP8266 happens over USB, reducing the risk of access point misuse.
- **Wi-Fi Network Scanning**: The app allows users to scan for nearby SSIDs and select the target for deauthentication.
- **Deauthentication Attack**: Perform deauth attacks on a chosen SSID to disconnect devices from the network.
- **Real-time Feedback**: The app provides continuous feedback from the ESP8266 via the serial interface.

## **Use Cases**

- **Network Testing**: Test the resilience of your network to deauthentication attacks.
- **Security Research**: Perform penetration testing and ethical hacking within legal bounds.
- **Learning Tool**: Understand the mechanics of deauthentication attacks and how to defend against them.

---

## **Setup and Installation**

### **1. Arduino Setup (ESP8266)**

Before running the Dauth Python application, you need to upload the ESP8266 firmware.

**Required Libraries:**
- ESP8266WiFi
- SpaceHuhn Deauther (Use the library by SpaceHuhn Technologies)

Upload the firmware using the Arduino IDE.

---

### **2. Python Application Setup**

The Dauth control app is a Python GUI built using Tkinter, which interacts with the ESP8266 over USB.

**Required Python Libraries:**

Install the necessary dependencies via pip:

```
pip install pyserial tkinter
```

Run the Python app after the Arduino setup:

```
python your_app.py
```

---

## **Running the Project**

1. **Upload the Arduino code** to your ESP8266 using the Arduino IDE.
2. **Run the Python App** using the command:

   ```
   python your_app.py
   ```

3. **Connect** to the ESP8266, input the correct password, and use the GUI to scan networks and perform deauth attacks.

---

## **Security Disclaimer**

This tool is intended for educational purposes and security testing of your own network. Ensure you have permission before running deauth attacks on any network. Misuse of this tool is illegal in many regions and can result in severe penalties.
