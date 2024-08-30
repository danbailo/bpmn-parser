class BPMNTagNotFound(Exception):
    def __init__(self, message: str = 'BPMN tag not found!'):
        super().__init__(message)


class NotBPMNFile(Exception):
    def __init__(self, message: str = 'The file is not a BPMN!'):
        super().__init__(message)
