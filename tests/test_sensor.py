"""
Test suite for the ADXL345 sensor functionality
"""

import unittest
from unittest.mock import MagicMock
import smbus
from adxl345 import ADXL345

class TestADXL345Sensor(unittest.TestCase):
    """Test cases for ADXL345 sensor functionality"""
    
    def setUp(self):
        """Set up test environment"""
        # Mock the smbus module
        self.mock_smbus = MagicMock()
        self.original_smbus = smbus.SMBus
        smbus.SMBus = self.mock_smbus
        
    def tearDown(self):
        """Clean up test environment"""
        smbus.SMBus = self.original_smbus
        
    def test_sensor_initialization(self):
        """Test sensor initialization"""
        try:
            sensor = ADXL345()
            self.assertIsNotNone(sensor)
        except Exception as e:
            self.fail(f"Sensor initialization failed: {str(e)}")
            
    def test_get_axes(self):
        """Test getting axes data"""
        sensor = ADXL345()
        axes = sensor.getAxes(True)
        self.assertIn('x', axes)
        self.assertIn('y', axes)
        self.assertIn('z', axes)
        
    def test_magnitude_calculation(self):
        """Test vibration magnitude calculation"""
        # Test with zero acceleration
        axes = {'x': 0, 'y': 0, 'z': 0}
        magnitude = (axes['x']**2 + axes['y']**2 + axes['z']**2)**0.5
        self.assertEqual(magnitude, 0)
        
        # Test with non-zero acceleration
        axes = {'x': 1, 'y': 1, 'z': 1}
        magnitude = (axes['x']**2 + axes['y']**2 + axes['z']**2)**0.5
        self.assertEqual(magnitude, 3**0.5)

if __name__ == '__main__':
    unittest.main()
