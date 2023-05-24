import datetime
import khayyam


class TimeStamp:
    """
        a base class for working with time in app
        ~!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!~
        #todo :
            add some utils for calculate and some stuff like that one dates
    """

    __now_gregorian = None
    __now_jalali = None
    __now_timestamp = None
    __now_time = None

    def __init__(self):
        # constructor method
        self.__now_jalali = self.now_jalali()
        self.__now_gregorian = self.now_gregorian()
        self.__now_timestamp = self.now_unixtime()
        self.__now_time = self.now_time()

    @property
    def time(self):
        """Return time That Object created"""
        return self.__now_time

    @property
    def georgian(self):
        """Return Gregorian time That Object created"""
        return self.__now_gregorian

    @property
    def jalali(self):
        """Return Jalali time That Object created"""
        return self.__now_jalali

    @property
    def timestamp(self):
        """Return timestamp time That Object created"""
        return self.__now_timestamp

    def now_time(self):
        """this method return now time"""
        return datetime.datetime.now().time()

    def now_unixtime(self):
        """this method return now time in unix time"""
        return int(datetime.datetime.now().timestamp())

    def now_gregorian(self):
        """this method return now time in gregorian time"""
        return datetime.date.today()

    def now_jalali(self):
        """this method return now time in jalali format"""
        return khayyam.JalaliDate.today()

    def convert_jlj2_georgian(self, value: khayyam.JalaliDate):
        """
            this method get a khayyam date<jalali> and convert it to gregorian object datetime.date
        """
        if not isinstance(value, khayyam.JalaliDate):
            raise ValueError("input must be a khayyam.JalaliDatetime instance")
        year, month, day = value.year, value.month, value.day
        date = self._jalali_to_gregorian(year, month, day)
        return datetime.date(year=date[0], month=date[1], day=date[2])

    def convert_grg2_jalali(self, value: datetime.date):
        """
            this method get a datetime.date object and convert it o khayyam object
        """
        if not isinstance(value, datetime.date):
            raise ValueError("input must be a khayyam.JalaliDatetime instance")
        year, month, day = value.year, value.month, value.day
        date = self._gregorian_to_jalali(year, month, day)
        return khayyam.JalaliDate(year=date[0], month=date[1], day=date[2])

    def _gregorian_to_jalali(self, gy, gm, gd):
        """
            this method convert a gregorian to a jalali date
        """
        g_d_m = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        if (gm > 2):
            gy2 = gy + 1
        else:
            gy2 = gy
        days = 355666 + (365 * gy) + ((gy2 + 3) // 4) - ((gy2 + 99) // 100) + ((gy2 + 399) // 400) + gd + g_d_m[gm - 1]
        jy = -1595 + (33 * (days // 12053))
        days %= 12053
        jy += 4 * (days // 1461)
        days %= 1461
        if (days > 365):
            jy += (days - 1) // 365
            days = (days - 1) % 365
        if (days < 186):
            jm = 1 + (days // 31)
            jd = 1 + (days % 31)
        else:
            jm = 7 + ((days - 186) // 30)
            jd = 1 + ((days - 186) % 30)
        return [jy, jm, jd]

    def _jalali_to_gregorian(self, jy, jm, jd):
        """
            this method convert a jalali time to a gregorian time
        """
        jy += 1595
        days = -355668 + (365 * jy) + ((jy // 33) * 8) + (((jy % 33) + 3) // 4) + jd
        if (jm < 7):
            days += (jm - 1) * 31
        else:
            days += ((jm - 7) * 30) + 186
        gy = 400 * (days // 146097)
        days %= 146097
        if (days > 36524):
            days -= 1
            gy += 100 * (days // 36524)
            days %= 36524
            if (days >= 365):
                days += 1
        gy += 4 * (days // 1461)
        days %= 1461
        if (days > 365):
            gy += ((days - 1) // 365)
            days = (days - 1) % 365
        gd = days + 1
        if ((gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0)):
            kab = 29
        else:
            kab = 28
        sal_a = [0, 31, kab, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        gm = 0
        while (gm < 13 and gd > sal_a[gm]):
            gd -= sal_a[gm]
            gm += 1
        return [gy, gm, gd]


    def bigger_date(self, date1, date2):
        """
            this method take two date and e return biggest
            :params: date1, date2
            - if both dates are equal return True
            - if date1 is biggest return date1
            - if date2 is biggest return date2
        """
        if date1 > date2:
            return date1
        elif date2 > date1:
            return date2
        else:
            return True

    def smaller_date(self, date1, date2):
        """
            this method take two date and e return smallets
            :params: date1, date2
            - if both dates are equal return True
            - if date1 is smallest return date1
            - if date2 is smallest return date2
        """
        if date1 < date2:
            return date1
        elif date2 < date1:
            return date2
        else:
            return True


