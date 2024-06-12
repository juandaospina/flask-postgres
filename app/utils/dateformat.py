from datetime import datetime

class DateFormat:
    @classmethod
    def convert_date(self, date):
        return datetime.strftime(date, '%d/%m/%Y')