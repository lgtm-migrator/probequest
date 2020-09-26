"""
Unit tests for the probe request sniffer module.
"""

import unittest

from probequest.config import Config
from probequest.probe_request_sniffer import ProbeRequestSniffer


class TestProbeRequestSniffer(unittest.TestCase):
    """
    Unit tests for the 'ProbeRequestSniffer' class.
    """

    def test_without_parameters(self):
        """
        Initialises a 'ProbeRequestSniffer' object without parameters.
        """

        # pylint: disable=no-value-for-parameter

        with self.assertRaises(TypeError):
            _ = ProbeRequestSniffer()

    def test_bad_parameter(self):
        """
        Initialises a 'ProbeRequestSniffer' object with a bad parameter.
        """

        # pylint: disable=no-value-for-parameter

        with self.assertRaises(AttributeError):
            _ = ProbeRequestSniffer("test")

    def test_create_sniffer(self):
        """
        Creates a 'ProbeRequestSniffer' object with the correct parameter.
        """

        # pylint: disable=no-self-use

        config = Config()
        _ = ProbeRequestSniffer(config)

    def test_stop_before_start(self):
        """
        Creates a 'ProbeRequestSniffer' object and stops the sniffer before
        starting it.
        """

        # pylint: disable=no-self-use

        config = Config()
        sniffer = ProbeRequestSniffer(config)
        sniffer.stop()
