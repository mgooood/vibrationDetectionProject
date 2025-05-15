# Raspberry Pi Vibration Detection System

This project detects vibrations using an ADXL345 sensor and takes pictures when vibrations are detected.

## Hardware Requirements

- Raspberry Pi 3B
- ADXL345 Accelerometer
- Raspberry Pi Camera
- Breadboard and jumper wires

## Software Requirements

- Python 3 (comes with Raspberry Pi)
- Required Python packages (listed in requirements.txt):
  - smbus: For I2C communication with the ADXL345 sensor
  - picamera: For controlling the Raspberry Pi camera
  - adxl345: Library for interfacing with the ADXL345 sensor
  - pytest: For running tests
  - pytest-mock: For mocking hardware interfaces in tests
  - coverage: For measuring test coverage

## Setup Instructions

1. Connect the ADXL345 sensor to the Raspberry Pi:
   - VCC to 3.3V
   - GND to GND
   - SDA to GPIO 3 (SDA)
   - SCL to GPIO 5 (SCL)

2. Connect the Pi Camera to the camera port on the Raspberry Pi

3. Install the required Python packages:
   ```bash
   # Install system package
   sudo apt install python3-smbus
   
   # Install Python packages from requirements.txt
   pip3 install -r requirements.txt
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
- `tests/`: Directory containing test files

## Testing

This project includes unit tests to verify the functionality of the vibration detection system.

### Running Tests

To run the tests, you need:
1. The Raspberry Pi hardware (ADXL345 sensor and Pi Camera)
2. All required dependencies installed

Run the tests using:
```bash
pytest tests/
```

To get test coverage:
```bash
coverage run -m pytest tests/
coverage report
```

### Mocking Hardware

Some tests can be run without hardware by mocking the sensor and camera interfaces. However, for complete testing, the hardware must be connected to the Raspberry Pi.

## Configuration

You can adjust the following settings in the script:
- `VIBRATION_THRESHOLD`: Adjust this value to set the sensitivity
- `LOG_FILE`: Name of the log file
- `PICTURE_DIR`: Directory for saving pictures

## Notes

- Make sure the I2C interface is enabled on your Raspberry Pi
- The script runs continuously until interrupted (Ctrl+C)
- Adjust the `VIBRATION_THRESHOLD` based on your specific needs and environment
- Some tests require hardware to be connected to the Raspberry Pi
- The ADXL345 sensor must be properly connected to the I2C bus
- The Pi Camera must be connected to the camera port
