import re
from datetime import datetime

from ilg.models.log_record import LogRecord


class LogParser:
    def parse(self, entry: list[str]) -> LogRecord:
        raw = "\n".join(entry)

        timestamp_text = raw[:23]
        timestamp = datetime.strptime(  # noqa: DTZ007
            timestamp_text,
            "%Y-%m-%d %H:%M:%S,%f",
        )

        level_match = re.search(
            r"\b(DEBUG|INFO|WARN|ERROR)\b",
            raw,
        )

        message = raw.rsplit(") ", 1)[-1]

        level = level_match.group(1) if level_match else None

        return LogRecord(
            timestamp=timestamp,
            level=level,
            message=message,
            raw=raw,
        )