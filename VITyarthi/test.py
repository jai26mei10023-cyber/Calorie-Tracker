import unittest
import os
import json
from auth import hash_password
from storage import save_json, load_json

class TestDietTracker(unittest.TestCase):
    def setUp(self):
        # Set up a temporary file for testing storage functions
        self.test_file = 'test_data_temp.json'

    def tearDown(self):
        # Clean up the temporary file after tests run
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_hash_password(self):
        password = "securepassword123"
        hashed = hash_password(password)
        
        # Verify the password is actually hashed
        self.assertNotEqual(password, hashed)
        # Verify it generates a 64-character SHA-256 string
        self.assertEqual(len(hashed), 64) 

    def test_storage_save_and_load(self):
        test_data = {"test_user": "hashed_pw_123"}
        
        # Test saving
        save_json(self.test_file, test_data)
        self.assertTrue(os.path.exists(self.test_file))
        
        # Test loading
        loaded_data = load_json(self.test_file)
        self.assertEqual(test_data, loaded_data)

    def test_load_nonexistent_file(self):
        # Verify the system handles missing files gracefully by returning an empty dict
        data = load_json("does_not_exist_file.json")
        self.assertEqual(data, {})

if __name__ == '__main__':
    unittest.main()