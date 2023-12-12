import random

class ScheduleGenerator:
    def __init__(self, data, days, periods):
        self.data = data
        self.days = days
        self.periods = periods
        self.schedule = {}

    def generate_schedule(self):
        for entry in self.data:
            professor, subject = entry
            day, period = self.assign_timeslot(professor, subject)

            if day is not None and period is not None:
                self.schedule[(day, period)] = {'Professor': professor, 'Subject': subject}
                alternate_day = self.get_alternate_day(day)
                alternate_period = period
                if (alternate_day, alternate_period) not in self.schedule:
                    self.schedule[(alternate_day, alternate_period)] = {'Professor': professor, 'Subject': subject}
            else:
                print(f"Failed to schedule {subject} with {professor}. Please check constraints.")

        while len(self.schedule) < 25:
            day, period = self.assign_timeslot("???", "???")
            if day is not None and period is not None:
                self.schedule[(day, period)] = {'Professor': "???", 'Subject': "???"}

    def assign_timeslot(self, professor, subject):
        available_slots = [(day, period) for day in self.days for period in self.periods if (day, period) not in self.schedule]
        available_slots = [(day, period) for (day, period) in available_slots if self.is_valid_slot(professor, day, period)]

        if available_slots:
            # 최적화를 위한 목적 함수를 적용하여 가장 좋은 슬롯을 선택
            best_slot = min(available_slots, key=lambda slot: self.objective_function(slot))
            return best_slot
        else:
            return None, None

    def is_valid_slot(self, professor, day, period):
        same_day_slots = [(d, p) for (d, p), info in self.schedule.items() if d == day and info['Professor'] == professor]
        if len(same_day_slots) >= 2:
            return False

        if day == "수" and period == "5":
            return professor == "???"

        return True

    def get_alternate_day(self, day):
        index = self.days.index(day)
        return self.days[(index + 1) % len(self.days)]

    def objective_function(self, slot):
        # 최적화를 위한 목적 함수 예시
        # 여기에 각종 제약 조건에 대한 평가 지표를 추가할 수 있습니다.
        return 0

# 주어진 데이터
sample = [
    ["고선우", "확률과통계"],
    ["고선우", "딥러닝"],
    ["권수태", "AI알고리즘"],
    ["권수태", "기계학습"],
    ["민정익", "AI수학"],
    ["민정익", "논리적문제해결1"],
    ["이근호", "인공지능기초"],
    ["이근호", "서비스러닝"],
    ["송주환", "논리적문제해결2"],
    ["송주환", "영상이해"],
    ["김영수", "AI프로그래밍"],
    ["김영수", "리눅스운영체제"]
]

# 요일과 교시 설정
days = ["월", "화", "수", "목", "금"]
periods = ["1", "2", "3", "4", "5"]

# 알고리즘 실행
schedule_generator = ScheduleGenerator(sample, days, periods)
schedule_generator.generate_schedule()

# 결과 출력
for (day, period), details in schedule_generator.schedule.items():
    print(f"{day}{period}: Professor {details['Professor']}, Subject {details['Subject']}")
