from pathlib import Path

from ilg.ingestor.log_ingestor import LogIngestor


def test_load_simple_log():
    log_file = Path(__file__).parent / "test_data" / "simple_test.log"

    ingestor = LogIngestor()
    lines = ingestor.load(log_file)

    for line in lines:
        print(line)