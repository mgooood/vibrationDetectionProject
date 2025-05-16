"""
Test suite for camera functionality
"""

import unittest
from unittest.mock import MagicMock, patch
from vibration_detector import take_picture
import os

class TestCamera(unittest.TestCase):
    """Test cases for camera functionality"""
    
    def setUp(self):
        """Set up test environment"""
        # Create mock Picamera2 class and methods
        self.mock_camera = MagicMock()
        self.mock_camera.create_still_configuration.return_value = {}
        
        # Patch the Picamera2 class
        self.patcher = patch('vibration_detector.Picamera2', return_value=self.mock_camera)
        self.mock_picamera2 = self.patcher.start()
        
    def tearDown(self):
        """Clean up test environment"""
        self.patcher.stop()
        
    def test_take_picture(self):
        """Test taking a picture"""
        timestamp = "test_timestamp"
        mock_camera = MagicMock()
        take_picture(mock_camera, timestamp)
        
        # Verify that the camera's capture_file method was called
        mock_camera.capture_file.assert_called_once()
        
    def test_picture_naming(self):
        """Test that pictures are named correctly"""
        timestamp = "20230515_160000"
        mock_camera = MagicMock()
        take_picture(mock_camera, timestamp)
        
        # Verify the picture was saved with the correct name
        expected_filename = f"vibration_{timestamp}.jpg"
        expected_path = os.path.join("vibration_output", "vibration_pictures", expected_filename)
        
        # Verify the camera's capture_file method was called with the correct path
        mock_camera.capture_file.assert_called_with(expected_path)

if __name__ == '__main__':
    unittest.main()
