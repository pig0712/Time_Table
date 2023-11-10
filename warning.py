class TimetableChecker:
    def __init__(self, filename):
        # 형운이가 줄 파일에서 읽은거 저장할 딕셔너리
        self.schedule = self.load_schedule(filename)

    def load_schedule(self, filename):
        # 형운이가 줄 파일 읽어와 딕셔너리 형태로 반환
        schedule = {}
        with open(filename, 'r') as file:
            for line in file:
                professor, day, time = line.strip().split(',')
                day = int(day)
                if professor in schedule:
                    schedule[professor].append((day, time))
                else:
                    schedule[professor] = [(day, time)]
        return schedule

    def check_alternate_days(self, professor):
        # 교수님 수업 일정이 없으면 False 반환
        if professor not in self.schedule:
            return False

        # 교수의 수업이 격일로 배정되었는지 확인
        days = set(day for day, _ in self.schedule[professor])
        for day in days:
            if (day + 2, 'time') not in self.schedule[professor]:
                return False

        return True

    def check_max_daily_classes(self, professor):
        # 교수의 수업 일정이 없으면 False 반환
        if professor not in self.schedule:
            return False

        # 하루 최대 수업 횟수가 3회를 초과하는지 확인
        for day in self.schedule[professor]:
            if len(self.schedule[professor][day]) >= 3:
                return False

        return True
