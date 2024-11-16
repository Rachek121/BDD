import sys
import unittest
from unittest.mock import MagicMock, patch
from PyQt6.QtWidgets import QApplication, QMessageBox
from app.addDataWin import AddDataWin  # Adjust the import as needed


class TestAddDataWin(unittest.TestCase):
    @patch('ui.addDataWin.Data')  # Adjust this patch for the Data class location
    def setUp(self, mock_data):
        self.app = QApplication(sys.argv)
        self.mock_db = MagicMock()  # Create a mock database object
        mock_data.return_value = self.mock_db  # Make sure it returns our mock object

        # Set up the instance of AddDataWin which now uses the mocked Data
        self.window = AddDataWin()

        # Mock the methods needed for the tests
        self.mock_db.get_work_types.return_value = [(1, "Test Work")]
        self.mock_db.get_executors.return_value = [(1, "Test Executor")]
        self.mock_db.get_statuses.return_value = [(1, "New")]

    def test_successful_add_record(self):
        # Test implementation here...
        pass

    def test_invalid_data_record(self):
        # Test implementation here...
        pass


if __name__ == '__main__':
    unittest.main()
