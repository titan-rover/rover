class Error(Exception):
    pass

class Serial_Port_Not_Active_Error(Error):
    def __init__(self, serial_path, seconds):
        self.message = f"ERROR: Serial Device at path {serial_path} not found, waiting {seconds} seconds to try again"

    def __str__(self):
        return self.message

class Serial_Read_Timeout_Error(Error):
    def __init__(self):
        self.message = "ERROR: Serial device data read timeout."

    def __str__(self):
        return self.message