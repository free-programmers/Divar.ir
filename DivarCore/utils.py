import datetime
import khayyam


class TimeStamp:
    """
        Time stamp class form convert a unix time stamp to georgian and jalali date
    """


    @property
    def now_unix(self):
        """
            this method return now time in unix time
        """
        return int(datetime.datetime.now().timestamp())

    def now_georgian(self):
        """
            this method return now time in georgian time
        """
        return datetime.datetime.now()

    def now_jalali(self):
        """
            this method return now time in jalali format
        """
        return khayyam.JalaliDatetime.now()

    def convert_jlj2_georgian(self, value: khayyam.JalaliDatetime):
        if not isinstance(value, khayyam.JalaliDatetime):
            raise ValueError("input must be a khayyam.JalaliDatetime instance")



