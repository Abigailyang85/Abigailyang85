import datetime

class ROCDate:  # 類別

    def __init__(self, datetime_obj):  # 初始化

        # obj, roc_year, month, day, ... 皆為屬性

        self.obj = datetime_obj
        self.roc_year = self.get_roc_year()
        self.month = self.obj.month
        self.day = self.obj.day
        self.hour = self.obj.hour
        self.minute = self.obj.minute
        self.second = self.obj.second
        self.microsecond = self.obj.microsecond
        self.tzinfo = self.obj.tzinfo

    def get_roc_year(self):  # 方法
        return self.obj.year - 1911
