from datetime import datetime, timezone


def main() -> None:
    print("network-outage-prediction-system initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
