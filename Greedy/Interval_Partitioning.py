# find minimum number of classrooms to schedule all lectures so that
# no two occur at the same time in the same room.

import heapq
iterative = True
# lectures = [(start_time,finish_time),...]
lectures = [(0,3),(0,3),(0,7),(4,7),(4,10),(8,11),(8,11),(10,15),(12,15),(12,15)]
lectures = sorted(lectures,key=lambda x:x[0])
classrooms = [(lectures[0][1],0)]
final_classrooms = [[lectures[0]]]
for lecture in lectures[1:]:
    if iterative:
        print('considered lecture:',lecture)
        print('lecture finish time for each classroom:',[elem[0] for elem in classrooms])
    if lecture[0]>=classrooms[0][0]:
        heapq.heappush(classrooms,(lecture[1],classrooms[0][1]))
        final_classrooms[classrooms[0][1]].append(lecture)
        heapq.heappop(classrooms)
    else:
        final_classrooms.append([lecture])
        heapq.heappush(classrooms,(lecture[1],len(final_classrooms)-1))
    print('Updated classroom list:',[elem[0] for elem in classrooms])
    _ = input()
print(f'd = {len(final_classrooms)}, Final classroom schedule:')
for classroom in final_classrooms:
    print(classroom)
