import matplotlib.pyplot as plt
import numpy as np

'''

miles = [8.087038516998291, 2.7357072830200195, 5.1903016567230225, 0.5659356117248535, 3.9650182723999023, 1.1998443603515625, 6.644936561584473, 13.477819681167603, 37.328054428100586, 1.7707195281982422, 0.7953941822052002, 1.3099493980407715, 33.957951068878174, 1.6824274063110352, 2.6690022945404053, 0.3437371253967285, 5141.358270406723, 1.4755942821502686, 2.025657892227173, 7161.031766414642, 6.486213207244873, 770.6436560153961]     
tyler = [4.931871175765991, 0.7580869197845459, 2.1330111026763916, 0.2460157871246338, 1.335273027420044, 0.6188688278198242, 2.1566710472106934, 3.1790928840637207, 9.113592863082886, 0.8682162761688232, 0.5500280857086182, 0.7007789611816406, 4.7685136795043945, 0.8314509391784668, 0.7309210300445557, 0.2554440498352051, 2142.893802881241, 0.7237188816070557, 0.9414811134338379, 3115.501879930496, 4.221510171890259, 332.6300082206726]     
tim = [4.895982265472412, 3.955394744873047, 2.5529165267944336, 0.6678829193115234, 4.612080335617065, 1.3541688919067383, 7.623936891555786, 16.15020251274109, 43.92676591873169, 2.012772560119629, 0.91286301612854, 1.4883439540863037, 30.564483880996704, 1.88138747215271, 2.97370982170105, 0.3749406337738037, 6174.37712097168, 1.6536986827850342, 2.3313944339752197, 8415.49659371376, 7.113042116165161, 921.7802448272705]
alferdo = [9.50284600257873, 1.60479092597961, 7.65275192260742, 3.25511288642883, 4.23113489151, 1.20351004600524, 3.66288518905639, 6.27565383911132, 16.1949760913848, 1.38910198211669, 1.32947778701782, 1.11569571495056, 11.3404140472412, 1.3922369480133, 1.20157694816589, 0.438530921936035, 3038.39306998252, 1.24212193489074, 1.29249000549316, 4309.46820878982, 6.06105613708496, 455.867128133773]
'''

labels = ['Q' + str(i) for i in range(1, 23)]

'''miles = [9.347817836812158, 8.416853932584267, 7.362908011869433, 14.618918918918922, 11.38062015503878, 11.88227848101265, 12.17528868360282, 13.268643101482304, 11.81733937397016, 12.0206896551724, 12.019230769230766, 11.537209302325573, 14.246944318696125, 12.379090909090902, 11.606896551724123, 12.782608695652176, 11.69117874881559, 11.134020618556686, 11.496969696969687, 11.825987623266744, 10.83167848699769, 11.564676775736851]
tyler = [0.04758392675483215, 0.018253968253968255, 0.009639953542392568, 0.054337899543379, 0.05848708487084871, 0.02581888246628131, 0.1020797227036395, 0.021646220815195887, 0.03625730994152047, 0.08457446808510638, 0.026769911504424777, 0.0, 0.05643120716921454, 0.01875, 0.18892617449664428, 0.04981412639405205, 0.04743460486741918, 0.07839195979899496, 0.10455729166666666, 0.04757374188736036, 0.03549645390070922, 0.057827045733669966]
tim = [17.732484076433163, 5.507450980392155, 15.037195121951234, 14.202325581395348, 11.640136054421808, 10.383908045977, 9.899173553719066, 15.825556631171262, 11.590544412607079, 9.581249999999983, 9.101694915254239, 9.350526315789464, 12.320679168778346, 9.560833333333319, 9.306349206349184, 10.112500000000004, 10.778192341386328, 9.100952380952366, 10.210135135135115, 10.110767161611342, 9.712168141592972, 9.98817285174399]
alferdo = [0.0400502197112366, 0.0217821782178217, 0.052978434625245, 0.00900423728813559, 0.0601331789229878, 0.0671656686626746, 0.0791319444444444, 0.105813492063492, 0.0396365613108643, 0.0087979094076655, 0.043677130044843, 0.0109051254089422, 0.061256135653726, 0.130935875216637, 0.135437881873727, 0.0, 0.0326548839097285, 0.0365525672371638, 0.0224705882352941, 0.0306283351812847, 0.018801912912157, 0.0309755559860778]
'''

miles = [52.5041745730551, 52.265168539325856, 52.26557863501472, 52.38108108108111, 52.32558139534861, 52.30000000000007, 52.299999999999585, 52.29885974914515, 52.28060131795897, 52.190517241379254, 52.19999999999998, 52.199999999999925, 52.33164327750167, 52.187272727272614, 52.19999999999997, 52.1826086956522, 47.55678977638844, 47.13402061855668, 47.19393939393929, 47.38824815226953, 47.40000000000006, 47.39235035915414]
tyler = [66.77332146490362, 67.71714285714296, 67.68414634146342, 68.20273972602712, 68.30000000000139, 68.29999999999974, 68.30000000000196, 68.29999999999876, 68.31420217209389, 68.4000000000009, 68.39358407079686, 68.30000000000013, 68.475276752769, 68.31962209302378, 68.30000000000015, 68.20334572490705, 68.70724540760389, 68.51943048576217, 68.56783854166568, 68.28474674282461, 67.31563829787031, 67.08575622410362]
tim = [49.503503184713225, 49.32431372549002, 49.31829268292685, 49.255813953488364, 49.24489795918402, 49.199999999999925, 49.20206611570289, 49.3879961277833, 49.759169054442054, 49.69999999999989, 49.69999999999997, 49.69999999999991, 49.7182970096293, 49.699999999999896, 49.69999999999999, 49.70000000000002, 43.19361455190539, 40.0, 40.0, 41.05490760324851, 42.100000000000016, 42.211420317624565]
alferdo = [56.3471311990033, 56.2625176803379, 56.2755089729979, 56.2999999999996, 56.3525188187586, 56.4000000000009, 56.3999999999969, 56.4000992063472, 56.4958841345034, 56.5, 56.5, 56.5, 56.5, 56.4282495667253, 56.5, 56.5, 57.0855016707876, 56.0, 56.0, 56.5257730429126, 55.7722376038287, 55.7864171718909]

x = np.arange(len(labels)) + 1  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x-0.4, miles, width, label='Miles') # x - width/2
rects2 = ax.bar(x-0.2, tyler, width, label='Tyler')
rects3 = ax.bar(x+0.2, tim, width, label='Tim')
rects4 = ax.bar(x+0.4, alferdo, width, label='Alferdo')

ax.set_xlabel('Queries')
ax.set_ylabel('RAM Percentage')
print(len(miles))
ax.set_xticks(x)
ax.legend()

plt.show()