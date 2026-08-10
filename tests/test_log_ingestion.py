from pathlib import Path

from ilg.ingestor.log_ingestor import LogIngestor
from ilg.ingestor.log_sanitizer import LogSanitizer


def test_simple_log_ingestor():
    log_file = Path(__file__).parent / "test_data" / "simple_test.log"

    ingestor = LogIngestor()
    sanitizer = LogSanitizer()

    lines = ingestor.load(log_file)
    lines = sanitizer.sanitize(lines)
    entries = sanitizer.split_entries(lines)

    for entry in entries:
        print("ENTRY:")
        for line in entry:
            print(line)
        print()