from pathlib import Path

from ilg.analyzer.log_parser import LogParser
from ilg.ingestor.log_ingestor import LogIngestor
from ilg.ingestor.log_sanitizer import LogSanitizer
from ilg.models.log_record import LogRecord


def test_simple_log_ingestor():
    log_file = Path(__file__).parent / "test_data" / "simple_test.log"

    ingestor = LogIngestor()
    sanitizer = LogSanitizer()
    parser = LogParser()

    lines = ingestor.load(log_file)
    lines = sanitizer.sanitize(lines)
    entries = sanitizer.split_entries(lines)

    records = [parser.parse(entry) for entry in entries]

    assert len(records) > 0

    for record in records:
        assert isinstance(record, LogRecord)

        print(record)