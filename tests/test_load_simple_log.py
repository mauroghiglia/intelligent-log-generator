from pathlib import Path


def test_load_simple_log():
    log_file = Path(__file__).parent / "test_data" / "simple_test.log"

    with log_file.open("r", encoding="utf-8") as file:
        content = file.read()

    print(content)