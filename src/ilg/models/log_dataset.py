from dataclasses import dataclass, field

from .log_record import LogRecord


@dataclass
class LogDataset:
    records: list[LogRecord] = field(default_factory=list)

    source: str | None = None