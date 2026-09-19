#!/usr/bin/env python3
"""Send a heartbeat after a successful local check; standard library only."""

from __future__ import annotations

import argparse
import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


def main() -> int:
    parser = argparse.ArgumentParser(description="Send a post-verification heartbeat.")
    parser.add_argument("--url", required=True)
    parser.add_argument("--status", choices=("pass", "fail"), required=True)
    parser.add_argument("--job", required=True)
    parser.add_argument("--timeout", type=float, default=10)
    args = parser.parse_args()

    payload = json.dumps({"job": args.job, "status": args.status}).encode("utf-8")
    request = Request(args.url, data=payload, headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urlopen(request, timeout=args.timeout) as response:
            print(json.dumps({"status": "sent", "http_status": response.status}))
            return 0 if 200 <= response.status < 300 else 1
    except (HTTPError, URLError, TimeoutError) as exc:
        print(f"heartbeat failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

