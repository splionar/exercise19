import rosbag
import sys

bag = rosbag.Bag(sys.argv[1])
#bag = rosbag.Bag('bag/example_rosbag_H3.bag')


dic = {}

def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (sum(s[n//2-1:n//2+1])/2.0, s[n//2])[n % 2] if n else None

def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)

for topic, msg, t in bag.read_messages():
	if topic not in dic:
		dic[topic] = []
		dic[topic].append(float(t.secs) + float(t.nsecs)/1000000000)
	else:
		dic[topic].append(float(t.secs) + float(t.nsecs)/1000000000)

print("\n")
for key in dic:
	t = dic[key]
	diff = [t[i+1]-t[i] for i in range(len(t)-1)]
	dic[key] = dic[key], diff
	Num_msgs = len(dic[key][0])
	Min = min(dic[key][1])
	Max = max(dic[key][1])
	Avg = mean(dic[key][1])
	Med = median(dic[key][1])
	print("{}:num_messages: {} period: min: {:.2f} max: {:.2f} average: {:.2f} median: {:.2f}").format(key, Num_msgs, Min, Max, Avg, Med)

print("\n")    
bag.close()
