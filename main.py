import database
import utils


def main():
    database.setup_database()
    utils.process_devision(56, devisor=0)
