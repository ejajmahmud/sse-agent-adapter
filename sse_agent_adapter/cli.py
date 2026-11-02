"""Command line interface for sse-agent-adapter."""
from .adapter import parse_sse_line

def main():
    line = 'data: {"choices": [{"delta": {"content": "Hello" }}]}'
    print("Parsed SSE:", parse_sse_line(line))

if __name__ == "__main__":
    main()
