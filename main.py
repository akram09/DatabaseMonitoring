from utils.env import load_environment_variables
from utils.logging import configure_logger


def main():
    load_environment_variables()
    configure_logger()


if __name__ == "__main__":
    main()
