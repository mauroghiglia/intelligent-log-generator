from pathlib import Path


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