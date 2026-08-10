from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class LogRecord:
    timestamp: datetime | None
    level: str | None
    message: str
    raw: str

    fields: dict[str, str] = field(default_factory=dict)

    source: str | None = None
    line_start: int | None = None
    line_end: int | None = None