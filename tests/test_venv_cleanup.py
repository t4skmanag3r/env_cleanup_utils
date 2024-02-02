import os
import shutil
import unittest
import tempfile
from env_cleanup_utils import (
    find_venv_dirs,
    find_pycache_dirs,
    find_node_modules_dirs,
    save_requirements,
    delete_venv,
    delete_pycache,
    delete_node_modules,
    testing,
)


class TestVenvCleanup(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()
        testing.create_sample_folder_structure(self.temp_dir)

    def tearDown(self):
        # Clean up the temporary directory
        shutil.rmtree(self.temp_dir)

    def test_find_venv_dirs(self):
        venv_dirs = find_venv_dirs(self.temp_dir)
        self.assertEqual(len(venv_dirs), 2)
        self.assertIn(os.path.join(self.temp_dir, "project1", ".venv"), venv_dirs)
        self.assertIn(os.path.join(self.temp_dir, "project2", "venv"), venv_dirs)

    def test_save_requirements(self):
        venv_dir = os.path.join(self.temp_dir, "project1", ".venv")

        # Create the virtual environment first
        testing.create_virtual_environment(venv_dir)

        save_requirements(venv_dir)
        requirements_file = os.path.join(self.temp_dir, "project1", "requirements.txt")
        self.assertTrue(os.path.exists(requirements_file))

    def test_find_pycache_dirs(self):
        venv_dirs = find_pycache_dirs(self.temp_dir)
        self.assertEqual(len(venv_dirs), 2)
        self.assertIn(os.path.join(self.temp_dir, "project1", "__pycache__"), venv_dirs)
        self.assertIn(
            os.path.join(self.temp_dir, "project2", "submodule", "__pycache__"),
            venv_dirs,
        )

    def test_find_node_moduleds_dirs(self):
        node_modules_dirs = find_node_modules_dirs(self.temp_dir)
        self.assertEqual(len(node_modules_dirs), 1)
        self.assertIn(
            os.path.join(self.temp_dir, "project2", "node_modules"), node_modules_dirs
        )

    def test_delete_venv(self):
        venv_dir = os.path.join(self.temp_dir, "project1", ".venv")
        delete_venv(venv_dir)
        self.assertFalse(os.path.exists(venv_dir))

    def test_delete_pycache(self):
        pycache1_dir = os.path.join(self.temp_dir, "project1", "__pycache__")
        pycache2_dir = os.path.join(
            self.temp_dir, "project2", "submodule", "__pycache__"
        )
        delete_pycache(pycache1_dir)
        delete_pycache(pycache2_dir)
        self.assertFalse(os.path.exists(pycache1_dir))
        self.assertFalse(os.path.exists(pycache2_dir))

    def test_delete_node_modules(self):
        node_modules_dir = os.path.join(self.temp_dir, "project2", "node_modules")
        delete_node_modules(node_modules_dir)
        self.assertFalse(os.path.exists(node_modules_dir))


if __name__ == "__main__":
    unittest.main()
