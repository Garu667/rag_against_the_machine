import sys
import fire
from src.cli import RagCLI


if __name__ == "__main__":
    try:
        fire.Fire(RagCLI)
    except KeyboardInterrupt:
        print("\nInterrupted.", file=sys.stderr)
        sys.exit(130)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
