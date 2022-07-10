class CustomDate:
    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def to_number(cls, date_str):
        try:
            return tuple(map(int, date_str.split('-')))
        except Exception:
            raise ValueError('Дата указана некорретно')

    @staticmethod
    def is_valid_date_str(date_str):
        try:
            nums = CustomDate.to_number(date_str)
        except Exception:
            return False

        # месяц — от 1 до 12
        if not (1 <= nums[1] <= 12):
            return False

        # год был с впередиидущим нулем
        if len(date_str.split('-').pop()) != len(str(nums[2])) or nums[2] <= 0:
            return False

        return True


ds = '01-01-2000'
print(CustomDate.to_number(ds))

d = CustomDate(ds)
print(d.to_number(ds))

print(d.is_valid_date_str(ds))
print(CustomDate.is_valid_date_str(ds))
