class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        
        def is_leapyear(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            if year % 4 == 0:
                return True

        weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
        
        days_cnt = 0
        for i in range(1971, year):
            days_cnt += 365
            if is_leapyear(i): 
                days_cnt += 1
        
        days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if is_leapyear(year):
            days_of_month[1] += 1
        for i in range(month - 1):
            days_cnt += days_of_month[i]

        days_cnt += day

        return weekdays[(days_cnt+3)%7]

