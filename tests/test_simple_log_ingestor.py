from pathlib import Path

from ilg.ingestor.log_ingestor import LogIngestor


def test_simple_log_ingestor():
    log_file = Path(__file__).parent / "test_data" / "simple_test.log"

    ingestor = LogIngestor()

    lines = ingestor.load(log_file)
    lines = ingestor.sanitize(lines)

    for line in lines:
        print(line)