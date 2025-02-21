import team_module as tmm
import attendance_module as atm
import task_module as tskm
import math
import datetime
import statistics

print(tmm.company)
print(tmm.introduce_developer())
print(tmm.introduce_manager())

print(atm.record_attendance('이현대','09'))
print(atm.record_leave('이현대','18'))

print(tskm.start_task('코딩'))
print(tskm.end_task('코딩'))

task = [10,12,8,15,9]
# another_mean = statistics.mean(task)
mean_task = math.ceil(sum(task)/len(task))

task_over = [x for x in task if (lambda x: x >= mean_task)(x)]
print(mean_task)
# print(another_mean)
print(task_over)

print(f'[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 토끼님이 {tskm.end_task("코드 리뷰")}')