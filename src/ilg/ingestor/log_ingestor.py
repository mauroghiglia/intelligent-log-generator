import re
from pathlib import Path

ENTRY_START_PATTERNS = [
    re.compile(r"^\d{8}_\d{6}:(DEBUG|INFO|WARN|ERROR):"),
    re.compile(
        r"^\d{4}-\d{2}-\d{2} "
        r"\d{2}:\d{2}:\d{2},\d{3}"
    ),
]


class LogIngestor:
    def load(self, file_path: str | Path) -> list[str]:
        path = Path(file_path)

        with path.open("r", encoding="utf-8") as file:
            return file.readlines()

    def sanitize(self, lines: list[str]) -> list[str]:
        sanitized = []

        for line in lines:
            line = line.rstrip("\r\n")

            if line:
                sanitized.append(line)

        return sanitized

    def is_entry_start(self, line: str) -> bool:
        return any(
            pattern.match(line)
            for pattern in ENTRY_START_PATTERNS
        )

    def split_entries(self, lines: list[str]) -> list[list[str]]:
        entries: list[list[str]] = []
        current_entry: list[str] = []

        for line in lines:
            if self.is_entry_start(line):
                if current_entry:
                    entries.append(current_entry)

                current_entry = [line]
            else:
                if current_entry:
                    current_entry.append(line)

        if current_entry:
            entries.append(current_entry)

        return entries