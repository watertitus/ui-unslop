import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts' / 'install.py'
spec = importlib.util.spec_from_file_location('ui_unslop_installer', SCRIPT)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)


class InstallerTests(unittest.TestCase):
    def test_install_both_in_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            paths = mod.install('both', 'project', project=tmp)
            self.assertEqual(len(paths), 2)
            for p in paths:
                self.assertTrue((p / 'SKILL.md').is_file())
                self.assertTrue((p / 'references' / '20-principles.md').is_file())
                self.assertIn('name: ui-unslop', (p / 'SKILL.md').read_text())

    def test_preserves_existing_without_force(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = mod.install('codex', 'project', project=tmp)[0]
            (p / 'local.txt').write_text('important')
            with self.assertRaises(FileExistsError):
                mod.install('codex', 'project', project=tmp)
            self.assertEqual((p / 'local.txt').read_text(), 'important')

    def test_preflight_prevents_partial_both_install(self):
        with tempfile.TemporaryDirectory() as tmp:
            mod.install('claude', 'project', project=tmp)
            with self.assertRaises(FileExistsError):
                mod.install('both', 'project', project=tmp)
            self.assertFalse((Path(tmp) / '.agents/skills/ui-unslop').exists())

    def test_force_reinstalls(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = mod.install('claude', 'project', project=tmp)[0]
            (p / 'old.txt').write_text('old')
            mod.install('claude', 'project', project=tmp, force=True)
            self.assertFalse((p / 'old.txt').exists())

    def test_user_install_custom_home(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = mod.install('codex', 'user', home=tmp)[0]
            self.assertEqual(p, Path(tmp) / '.agents/skills/ui-unslop')

if __name__ == '__main__':
    unittest.main()
