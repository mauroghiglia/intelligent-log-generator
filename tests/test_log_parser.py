from datetime import datetime

from ilg.analyzer.log_parser import LogParser


def test_parse_quarkus_log():
    parser = LogParser()

    entry = [
        (
            "2026-08-07 10:30:00,559 k70b60c8 <unknown>[5212] INFO  "
            "[CTE.PRI.CCP.TO.CCG.Q] "
            "(Camel (camel-1) thread #1 - "
            "JmsConsumer[CTE2.PRICES.CCPRO.TO.CCG.Q]) "
            "Start Process Message"
        )
    ]

    record = parser.parse(entry)

    assert record.timestamp == datetime(  # noqa: DTZ001
        2026, 8, 7, 10, 30, 0, 559000
    )
    assert record.level == "INFO"
    assert record.message == "Start Process Message"

    print(record)

def test_multiline_log_entry():
    lines = [
        "2026-08-07 10:30:00,559 k70b60c8 <unknown>[5212] INFO  [CTE.PRI.CCP.TO.CCG.Q] Start Process Message",
        "This is a continuation line",
    ]

    assert len(lines) == 2

def test_parse_all_groups_multiline_entries():
    parser = LogParser()

    lines = [
        "2026-08-07 10:30:00,559 k70b60c8 <unknown>[5212] INFO  [CTE.PRI.CCP.TO.CCG.Q] Start Process Message",
        "Continuation line",
        "2026-08-07 10:30:00,564 k70b60c8 <unknown>[5212] INFO  [CTE.PRI.CCP.TO.CCG.Q] End Process Message",
    ]

    records = parser.parse_all(lines)

    assert len(records) == 2