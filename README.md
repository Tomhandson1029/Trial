Weather Station with Adafruit
Welcome to the Weather Station with Adafruit project! This project combines IoT technology, environmental sensing, and web development to create a comprehensive weather monitoring system. Using an Adafruit Feather HUZZAH ESP8266 and a BME280 sensor, this weather station collects real-time data on temperature, humidity, and pressure. The data is then displayed on an OLED screen and can be uploaded to the Adafruit IO platform for remote monitoring. Additionally, the project features a web interface for data visualization and management.

Features
🌡 Real-Time Environmental Sensing: Collect temperature, humidity, and pressure data.
📡 WiFi Connectivity: Upload sensor data to Adafruit IO for IoT applications.
🌐 Web Interface: Visualize data through a custom web page, including real-time updates.
📊 Database Management: Store historical sensor data for trend analysis.
🔒 Automated Testing: Ensure reliability of the web platform with Selenium tests.
🛠 Easy Customization: Tailor the project to meet specific monitoring needs.
Components
Adafruit Feather HUZZAH ESP8266
BME280 sensor for temperature, humidity, and pressure
OLED Display
Breadboard and jumper wires
Setup and Installation
Hardware Assembly: Connect the BME280 sensor and OLED display to the ESP8266 according to the wiring diagram provided in the docs/ directory.
Software Configuration: Upload the provided Arduino sketch (Weather_Station.ino) to the ESP8266.
Web and Database Setup: Deploy the PHP scripts on your web server and create the MySQL database using the provided schema.
Adafruit IO Setup: Create an account on Adafruit IO and configure the feed for receiving sensor data.
Usage
The OLED display will show real-time sensor readings once the device is powered up.
Data is uploaded to Adafruit IO automatically for remote monitoring.
Access the web interface via your web server's URL to view historical data and trends.
Contributing
Contributions to the Weather Station with Adafruit project are welcome! Please submit pull requests or open issues to suggest improvements or report bugs.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

Weather Station Preview

🔗 Helpful Links

Adafruit Feather HUZZAH ESP8266
Adafruit IO
BME280 Sensor Guide
📞 Support

For support, please open an issue in the GitHub repository or reach out to us via the Adafruit forums.

Thank you for exploring the Weather Station with Adafruit project!
