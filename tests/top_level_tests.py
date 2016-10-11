import unittest2
import tfstate
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
EXAMPLE_DIR_PATH = os.path.abspath(os.path.join(CURRENT_DIR, '../examples'))
SIMPLE_EXAMPLE_STATE_PATH = os.path.join(EXAMPLE_DIR_PATH,
                                         'simple/terraform.tfstate')
SIMPLE_EXAMPLE_STATE_URI = 'file://%s' % SIMPLE_EXAMPLE_STATE_PATH
WITH_MODULES_EXAMPLE_STATE_PATH = os.path.join(EXAMPLE_DIR_PATH, 'with_modules/terraform.tfstate')
WITH_MODULES_EXAMPLE_STATE_URI = 'file://%s' % WITH_MODULES_EXAMPLE_STATE_PATH


class TopLevelTests(unittest2.TestCase):
    def test_get_state_against_simple_example(self):
        """Test tfstate against the example/ directory in this repository"""

        state_dict = tfstate.get(SIMPLE_EXAMPLE_STATE_URI)
        self.assertEqual(state_dict['test_list'], '1,2,3',
                         'Should have expected comma separated values')
        self.assertEqual(state_dict['test_string'], 'hello',
                         'Should have expected string')

    def test_get_state_against_module_example(self):
        root_state_dict = tfstate.get(WITH_MODULES_EXAMPLE_STATE_URI)

        self.assertEqual(root_state_dict['test_string_from_root'], 'hello_from_root',
                         'should have expected string')

        module_state_dict = tfstate.get(WITH_MODULES_EXAMPLE_STATE_URI, module='test_module')

        self.assertEqual(module_state_dict['test_string_from_module'], 'hello_from_module',
                         'should have expected string')
