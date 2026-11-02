"""Unit tests for SSE adapter."""
import unittest
from sse_agent_adapter.adapter import parse_sse_line

class TestSSE(unittest.TestCase):
    def test_parse_openai_sse(self):
        line = 'data: {"choices": [{"delta": {"content": "world"}}]}'
        res = parse_sse_line(line)
        self.assertEqual(res["delta"], "world")
        self.assertFalse(res["done"])

    def test_done_marker(self):
        res = parse_sse_line("data: [DONE]")
        self.assertTrue(res["done"])

if __name__ == "__main__":
    unittest.main()
