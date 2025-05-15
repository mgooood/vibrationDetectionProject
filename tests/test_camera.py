"""
Test suite for camera functionality
"""

import unittest
from unittest.mock import MagicMock
import picamera
from vibration_detector import take_picture

class TestCamera(unittest.TestCase):
    """Test cases for camera functionality"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock the picamera module
        self.mock_camera = MagicMock()
        self.original_camera = picamera.PiCamera
        picamera.PiCamera = self.mock_camera
        
    def tearDown(self):
        """Clean up test environment"""
        picamera.PiCamera = self.original_camera
        
    def test_take_picture(self):
        """Test taking a picture"""
        timestamp = "test_timestamp"
        take_picture(timestamp)
        
        # Verify that the camera's capture method was called
        self.mock_camera().capture.assert_called_once()
        
    def test_picture_naming(self):
        """Test that pictures are named correctly"""
        timestamp = "20230515_160000"
        take_picture(timestamp)
        
        # Verify the picture was saved with the correct name
        expected_filename = f"vibration_{timestamp}.jpg"
        expected_path = os.path.join("vibration_output", "vibration_pictures", expected_filename)
        
        # Verify the camera's capture method was called with the correct path
        self.mock_camera().capture.assert_called_with(expected_path)

if __name__ == '__main__':
    unittest.main()
