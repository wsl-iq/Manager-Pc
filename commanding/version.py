def version_App():
    __version__ = "3.2.1"
    __release_date__ = "Copyright (c) 2024-2025"
    __description__ = "This is the second release of the application with new features and improvements."
    __author__ = "Mohammed Al-Baqer"
    __status__ = "Stable"
    print("\033[97;1m")
    print('Version : ' + __version__)
    print('Release Date : ' + __release_date__)
    print('Description : ' + __description__)
    print('Author : ' + __author__)
    print('Status : ' + __status__)
if __name__ == "__main__":
    version_App()
