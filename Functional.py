##how to use enums
from enum import Enum

class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4

class CSVExporter:
    def __init__(self):
        self.status = CSVExportStatus.PENDING  # Initial state
        self.data = []
    
    def start_processing(self):
        self.status = CSVExportStatus.PROCESSING
        
    def mark_complete(self):
        self.status = CSVExportStatus.SUCCESS

# Usage
my_export = CSVExporter()
print(my_export.status)  # Shows: CSVExportStatus.PENDING
print(my_export.status.value)  # Shows: 1

my_export.start_processing()
print(my_export.status)  # Shows: CSVExportStatus.PROCESSING
print(my_export.status.value)  # Shows: 2

### other enum uses 

from enum import Enum


class DocFormat(Enum):
    PDF = 1
    TXT = 2
    MD = 3
    HTML = 4


# don't touch above this line


def convert_format(content, from_format, to_format):
    match (from_format, to_format):
        case (DocFormat.MD, DocFormat.HTML):
            return content.replace('# ','<h1>') + '</h1>'
        case (DocFormat.TXT, DocFormat.PDF):
            return f"[PDF] {content} [PDF]"
        case (DocFormat.HTML, DocFormat.MD):
            return content.replace('<h1>', '# ').replace('</h1>', '')
        case _:
            raise Exception("Invalid type")