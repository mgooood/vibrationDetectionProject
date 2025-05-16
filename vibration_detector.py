"""
Vibration Detector for Raspberry Pi with ADXL345 and Pi Camera

This script:
1. Reads vibration data from ADXL345 sensor
2. Logs vibration data with timestamps
3. Takes pictures when vibrations are detected
4. Names files based on vibration events

Dependencies:
- python3-smbus for ADXL345 communication
- picamera for camera functionality
"""

import time
import datetime
import os
import smbus
from picamera2 import Picamera2

# Import ADXL345 class from a local module
class ADXL345:
    """
    Local ADXL345 implementation that matches the expected interface.
    This is a placeholder - in a real implementation, this would be the actual ADXL345 driver.
    """
    def __init__(self):
        self.bus = smbus.SMBus(1)  # 1 indicates /dev/i2c-1
        # Initialize the ADXL345
        self.bus.write_byte_data(0x53, 0x2D, 0x08)  # Power control
        self.bus.write_byte_data(0x53, 0x31, 0x0B)  # Data format control
        self.bus.write_byte_data(0x53, 0x2C, 0x09)  # Rate

    def getAxes(self, gforce=False):
        """Get acceleration data for all axes"""
        bytes = self.bus.read_i2c_block_data(0x53, 0x32, 6)
        x = bytes[0] | (bytes[1] << 8)
        if x > 32767: x -= 65536
        y = bytes[2] | (bytes[3] << 8)
        if y > 32767: y -= 65536
        z = bytes[4] | (bytes[5] << 8)
        if z > 32767: z -= 65536
        
        # Convert to G's
        x = x * 0.004 * 9.80665 if gforce else x * 0.004
        y = y * 0.004 * 9.80665 if gforce else y * 0.004
        z = z * 0.004 * 9.80665 if gforce else z * 0.004
        
        return {'x': x, 'y': y, 'z': z}
# It handles all the low-level I2C communication and data conversion for us
# Without this library, we would need to write complex I2C communication code ourselves

# Configuration constants
OUTPUT_DIR = "vibration_output"  # Main output directory
LOG_FILE = os.path.join(OUTPUT_DIR, "vibration_log.txt")
PICTURE_DIR = os.path.join(OUTPUT_DIR, "vibration_pictures")
VIBRATION_THRESHOLD = 10  # Adjust this value based on your needs

# Initialize the ADXL345 sensor
def init_sensor():
    """Initialize the ADXL345 sensor and return the sensor object
    
    Returns:
        ADXL345: The initialized sensor object
    """
    try:
        sensor = ADXL345()
        print("ADXL345 sensor initialized successfully")
        return sensor
    except Exception as e:
        print(f"Error initializing sensor: {str(e)}")
        return None

# Initialize the camera
def init_camera():
    """Initialize the Pi Camera
    
    Returns:
        Picamera2: The initialized camera object
    """
    try:
        camera = Picamera2()
        # Configure camera with default still configuration
        camera_config = camera.create_still_configuration()
        camera.configure(camera_config)
        camera.start()
        print("Camera initialized successfully")
        return camera
    except Exception as e:
        print(f"Error initializing camera: {str(e)}")
        return None

# Create necessary directories
def setup_directories():
    """Create the necessary directories for storing pictures and logs
    """
    try:
        # Create picture directory if it doesn't exist
        if not os.path.exists(PICTURE_DIR):
            os.makedirs(PICTURE_DIR)
            print(f"Created directory: {PICTURE_DIR}")
            
        # Create log file if it doesn't exist
        if not os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'w') as f:
                f.write("Vibration Log File\n")
            print(f"Created log file: {LOG_FILE}")
    except Exception as e:
        print(f"Error setting up directories: {str(e)}")

def log_vibration(magnitude, timestamp):
    """Log vibration data to file
    
    Args:
        magnitude (float): The magnitude of the vibration
        timestamp (str): The timestamp of the vibration
    """
    try:
        with open(LOG_FILE, 'a') as f:
            f.write(f"{timestamp} - Vibration detected: {magnitude}\n")
        print(f"Logged vibration: {magnitude} at {timestamp}")
    except Exception as e:
        print(f"Error writing to log file: {str(e)}")

def take_picture(timestamp):
    """Take a picture and save it with a timestamp in the filename
    
    Args:
        timestamp (str): The timestamp to use in the filename
    """
    try:
        picture_name = f"vibration_{timestamp}.jpg"
        picture_path = os.path.join(PICTURE_DIR, picture_name)
        # Capture and save the image
        camera.capture_file(picture_path)
        print(f"Picture taken and saved as: {picture_name}")
    except Exception as e:
        print(f"Error taking picture: {str(e)}")

def main():
    """Main function that runs the vibration detection system
    """
    print("Starting Vibration Detection System...")
    
    # Initialize components
    sensor = init_sensor()
    if not sensor:
        print("Failed to initialize sensor. Exiting.")
        return
        
    camera = init_camera()
    if not camera:
        print("Failed to initialize camera. Exiting.")
        return
        
    setup_directories()
    
    print("System initialized. Waiting for vibrations...")
    
    try:
        while True:
            # Read acceleration data
            axes = sensor.getAxes(True)
            
            # Calculate magnitude (simple Euclidean distance)
            magnitude = (axes['x']**2 + axes['y']**2 + axes['z']**2)**0.5
            
            # Check if vibration exceeds threshold
            if magnitude > VIBRATION_THRESHOLD:
                # Get current timestamp
                timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                
                # Log the vibration
                log_vibration(magnitude, timestamp)
                
                # Take a picture
                take_picture(timestamp)
                
                # Add a small delay to avoid multiple triggers
                time.sleep(2)
            
            # Small delay between readings
            time.sleep(0.1)
            
    except KeyboardInterrupt:
        print("\nSystem stopped by user")
    finally:
        # Clean up
        if camera:
            camera.close()
            print("Camera closed")

if __name__ == "__main__":
    main()
