class Hash_Table:

    def __init__(self, size):
        self.size = size
        self.contents = {}

    def hash(self, key):
        if isinstance(key, str):
            total = 0
            for char in key:
                total += ord(char)
            return total % self.size
        else:
            raise TypeError('Key must be a string')

    def set(self, key, value):
        bucket = self.hash(key)
        if self.contents.get(bucket, None) is None:
            self.contents[bucket] = {key: value}
        else:
            self.contents[bucket][key] = value

    def lookup(self, key):
        bucket = self.hash(key)
        if self.contents.get(bucket, None) is not None:
            if self.contents[bucket].get(key, None) is not None:
                return self.contents[bucket][key]
            else:
                raise ValueError('No such key')
        else:
            raise ValueError('No such key')
