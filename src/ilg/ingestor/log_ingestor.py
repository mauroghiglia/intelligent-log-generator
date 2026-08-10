from pathlib import Path


class LogIngestor:
    def load(self, file_path: str | Path) -> list[str]:
        path = Path(file_path)

        records = []

        with path.open("r", encoding="utf-8") as file:
            for line in file:
                records.append(line.rstrip("\n"))

        return records