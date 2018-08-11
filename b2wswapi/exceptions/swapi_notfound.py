class SWAPINotFound(Exception):
    status_code = 404

    def __init__(self, message, status_code=None, payload=None):
        super().__init__(self)

        self.message = message
        self.payload = payload

        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        if self.payload is not None:
            r = dict(self.payload)
        else:
            r = {}
        r['message'] = self.message
        return r
