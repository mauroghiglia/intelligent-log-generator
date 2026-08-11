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

    def parse_all(self, lines: list[str]) -> list[LogRecord]:
        entries: list[list[str]] = []
        current_entry: list[str] = []

        for line in lines:
            if re.match(r"^\d{4}-\d{2}-\d{2} ", line):
                if current_entry:
                    entries.append(current_entry)

                current_entry = [line]
            else:
                current_entry.append(line)

        if current_entry:
            entries.append(current_entry)

        return [self.parse(entry) for entry in entries]