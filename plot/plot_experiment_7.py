import matplotlib.pyplot as plt
import numpy as np

def autolabel(rects, data):
    for rect, val in zip(rects, data):
        height = rect.get_height()
        ax.annotate('{}'.format(val),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')

BENCHMARK = 'RF'  # Sort, Join, RF

sort_throughputs = [137340726, 128996309, 133862600]
join_throughputs = [130904746, 148616525, 138840306]
rf_throughputs   = [15200433, 14290428, 10389722]

m5xlarge_cost  = 0.192
m6gxlarge_cost = 0.154
m5axlarge_cost = 0.172

sort_duration = ["237s", "252s", "243s"]
join_duration = ["145s", "127s", "136s"]
rf_duration   = ["1578s", "1679s", "2310s"]

colors = ['skyblue', 'lightcoral', 'lightgreen']

fig, ax = plt.subplots()

bar_width = 0.20

if BENCHMARK == 'Sort':
    rects1 = ax.bar(1 - bar_width * 1.05, [sort_throughputs[0]], bar_width, label='m5.xlarge | 0.192 per hour', color=colors[0], hatch='/')
    rects2 = ax.bar(1, [sort_throughputs[1]], bar_width, label='m6g.xlarge | 0.154 per hour', color=colors[1], hatch='\\')
    rects3 = ax.bar(1 + bar_width * 1.05, [sort_throughputs[2]], bar_width, label='m5a.xlarge | 0.172 per hour', color=colors[2], hatch='x')
    autolabel(rects1, [sort_duration[0]])
    autolabel(rects2, [sort_duration[1]])
    autolabel(rects3, [sort_duration[2]])

elif BENCHMARK == 'Join':
    rects4 = ax.bar(1 - bar_width * 1.05, [join_throughputs[0]], bar_width, label='m5.xlarge | 0.192 per hour', color=colors[0], hatch='/')
    rects5 = ax.bar(1, [join_throughputs[1]], bar_width, label='m6g.xlarge | 0.154 per hour', color=colors[1], hatch='\\')
    rects6 = ax.bar(1 + bar_width * 1.05, [join_throughputs[2]], bar_width, label='m5a.xlarge | 0.172 per hour', color=colors[2], hatch='x')
    autolabel(rects4, [join_duration[0]])
    autolabel(rects5, [join_duration[1]])
    autolabel(rects6, [join_duration[2]])

elif BENCHMARK == 'RF':
    rects7 = ax.bar(1 - bar_width * 1.05, [rf_throughputs[0]], bar_width, label='m5.xlarge | 0.192 per hour', color=colors[0], hatch='/')
    rects8 = ax.bar(1, [rf_throughputs[1]], bar_width, label='m6g.xlarge | 0.154 per hour', color=colors[1], hatch='\\')
    rects9 = ax.bar(1 + bar_width * 1.05, [rf_throughputs[2]], bar_width, label='m5a.xlarge | 0.172 per hour', color=colors[2], hatch='x')
    autolabel(rects7, [rf_duration[0]])
    autolabel(rects8, [rf_duration[1]])
    autolabel(rects9, [rf_duration[2]])

ax.set_xlabel(BENCHMARK + ' Benchmark')
ax.set_ylabel('Throughput (B/s)')

if BENCHMARK == 'Sort':
    ax.set_ylim(0, max(sort_throughputs) + 50000000)
elif BENCHMARK == 'Join':
    ax.set_ylim(0, max(join_throughputs) + 50000000)
elif BENCHMARK == 'RF':
    ax.set_ylim(0, max(rf_throughputs)   + 5000000)
ax.set_xticks([])
ax.legend()
plt.tight_layout()
plt.savefig('figures/' + 'experiment_7_' + BENCHMARK + '_results.png')
plt.show()
