import datetime as dt
import decimal
import json
from dataclasses import asdict
from typing import Any

from seedwork.domain import Entity


class ExtendedEncoder(json.JSONEncoder):
    def default(self, o: Any) -> Any:
        if isinstance(o, dt.datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, dt.date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, decimal.Decimal):
            return float(o)
        elif isinstance(o, Entity):
            return asdict(o)
        return json.JSONEncoder.default(self, o)


def loads(o: str) -> Any:
    return json.loads(o)


def dumps(o: Any, ensure_ascii: bool = False, indent: int = 0) -> str:
    return json.dumps(
        o,
        ensure_ascii=ensure_ascii,
        cls=ExtendedEncoder,
        separators=(',', ':'),
        indent=indent,
    )
