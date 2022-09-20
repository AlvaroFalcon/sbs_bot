
import command_manager
import unittest

class TestCommandManagerMethods(unittest.TestCase):

    def test_should_return_true_when_waifu_command_is_received(self):
        self.assertEqual(command_manager.is_command("wafiu"), False)
        self.assertEqual(command_manager.is_command("waifu"), False)
        self.assertEqual(command_manager.is_command("!waifu"), True)

if __name__ == '__main__':
    unittest.main()        