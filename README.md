# Raspberry Pi Vibration Detection System

This project detects vibrations using an ADXL345 sensor and takes pictures when vibrations are detected.

## Hardware Requirements

- Raspberry Pi 3B
- ADXL345 Accelerometer
- Raspberry Pi Camera
- Breadboard and jumper wires

## Software Requirements

- Python 3 (comes with Raspberry Pi)
- Required Python packages:
  - smbus
  - picamera
  - adxl345

## Setup Instructions

1. Connect the ADXL345 sensor to the Raspberry Pi:
   - VCC to 3.3V
   - GND to GND
   - SDA to GPIO 3 (SDA)
   - SCL to GPIO 5 (SCL)

2. Connect the Pi Camera to the camera port on the Raspberry Pi

3. Install the required Python packages:
   ```bash
   sudo apt-get install python3-smbus
   sudo pip3 install picamera
   sudo pip3 install adxl345
   ```

4. Run the script:
   ```bash
   python3 vibration_detector.py
   ```

## How It Works

1. The script continuously monitors the ADXL345 sensor
2. When a vibration above the threshold is detected:
   - The vibration magnitude is logged with a timestamp
   - A picture is taken and saved with a timestamp in the filename
3. All vibration data is logged in `vibration_log.txt`
4. Pictures are saved in the `vibration_pictures` directory

## File Structure

- `vibration_detector.py`: The main Python script
- `vibration_log.txt`: Log file containing vibration data
- `vibration_pictures/`: Directory where pictures are saved

## Configuration

You can adjust the following settings in the script:
- `VIBRATION_THRESHOLD`: Adjust this value to set the sensitivity
- `LOG_FILE`: Name of the log file
- `PICTURE_DIR`: Directory for saving pictures

## Notes

- Make sure the I2C interface is enabled on your Raspberry Pi
- The script runs continuously until interrupted (Ctrl+C)
- Adjust the `VIBRATION_THRESHOLD` based on your specific needs and environment
