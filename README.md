# Raspberry Pi Vibration Detection System

This project detects vibrations using an ADXL345 sensor and takes pictures when vibrations are detected.

## Hardware Requirements

- Raspberry Pi 3B
- ADXL345 Accelerometer
- Raspberry Pi Camera
- Breadboard and jumper wires

## Software Requirements

- Python 3 (comes with Raspberry Pi)
- Required system packages (installed via apt):
  - python3-smbus: System-level I2C interface for Python 3
  - python3-picamera2: Modern Python library for controlling the Raspberry Pi camera
  - python3-libcamera: Required camera support library
  - python3-adxl345: Library for interfacing with the ADXL345 sensor
  - python3-pytest: For running tests
  - python3-pytest-mock: For mocking hardware interfaces in tests
  - python3-coverage: For measuring test coverage

## Setup Instructions

1. Connect the ADXL345 sensor to the Raspberry Pi:
   - VCC to 3.3V
   - GND to GND
   - SDA to GPIO 3 (SDA)
   - SCL to GPIO 5 (SCL)

2. Connect the Pi Camera to the camera port on the Raspberry Pi

3. Install all required system packages:
   ```bash
   # Update package lists and install required packages
   sudo apt update
   sudo apt install -y \
       python3-smbus \
       python3-picamera2 \
       python3-libcamera \
       python3-adxl345 \
       python3-pytest \
       python3-pytest-mock \
       python3-coverage
   ```
   
   Note: All dependencies are installed via the system package manager for better compatibility with Raspberry Pi OS.

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
