class UnchainedException(Exception):
    def __init__(self):
        super(UnchainedException, self).__init__(self.message)


class DoesntExist(UnchainedException):
    message = "Attempting to get data by a key that doesn't exist"
