import sys

from src import game


def main() -> None:
    """Entry point to the game TicTacToe."""
    try:
        game.run()
    except Exception as exc:  # noqa: BLE001
        print(f"Произошла непредвиденная ошибка: {exc}")
        sys.exit(-1)


if __name__ == "__main__":
    main()
