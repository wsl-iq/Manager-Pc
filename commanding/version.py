def version_App():
    __version__ = "3.1.0"
    __release_date__ = "2025-01-09"
    __description__ = "This is the second release of the application with new features and improvements."
    __author__ = "Mohammed Al-Baqer"
    __email__ = "example@example.com"
    __status__ = "Stable"
    print("\033[97;1m")
    print(__version__)
    print(__release_date__)
    print(__description__)
    print(__author__)
    print(__email__)
    print(__status__)
if __name__ == "__main__":
    version_App()
