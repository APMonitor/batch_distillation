from apm import *
s = 'http://byu.apmonitor.com'
a = 'distill_l1_norm'
apm(s,a,'clear all')
apm_load(s,a,'distill.apm')
csv_load(s,a,'data.csv')
apm_option(s,a,'nlc.imode',5)
apm_option(s,a,'nlc.max_iter',100)
apm_option(s,a,'nlc.nodes',2)
apm_option(s,a,'nlc.time_shift',0)
apm_option(s,a,'nlc.ev_type',1)
apm_info(s,a,'FV','hf')
apm_info(s,a,'FV','vf')
apm_info(s,a,'FV','tray_hol')
apm_info(s,a,'FV','condenser_hol')
apm_info(s,a,'CV','x[1]')
apm_info(s,a,'CV','np')
output = apm(s,a,'solve')
print(output)
apm_option(s,a,'hf.status',1)
apm_option(s,a,'vf.status',1)
apm_option(s,a,'tray_hol.status',1)
apm_option(s,a,'condenser_hol.status',1)
apm_option(s,a,'x[1].fstatus',1)
apm_option(s,a,'np.fstatus',1)
apm_option(s,a,'x[1].wsphi',10000)
apm_option(s,a,'x[1].wsplo',10000)
apm_option(s,a,'np.wsphi',10)
apm_option(s,a,'np.wsplo',10)
apm_option(s,a,'x[1].meas_gap',1e-4)
apm_option(s,a,'np.meas_gap',0.01)
apm_option(s,a,'hf.lower',0.001);
apm_option(s,a,'hf.upper',1.0);
apm_option(s,a,'vf.lower',0.001);
apm_option(s,a,'vf.upper',0.6);
apm_option(s,a,'tray_hol.lower',0.01);
apm_option(s,a,'tray_hol.upper',0.1);
apm_option(s,a,'condenser_hol.lower',0.1)
apm_option(s,a,'condenser_hol.upper',0.5)
output = apm(s,a,'solve')
print(output)
y = apm_sol(s,a)
print('hf: ' + str(y['hf'][-1]))
print('vf: ' + str(y['vf'][-1]))
print('tray_hol: ' + str(y['tray_hol'][-1]))
print('cond_hol: ' + str(y['condenser_hol'][-1]))
print('np: ' + str(y['np'][-1]))
print('xp: ' + str(y['xp'][-1]))

import matplotlib.pyplot as plt
import pandas as pd
data_file = pd.read_csv('data_for_plotting.csv')

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(y['time'],y['np'],'bx-',linewidth=2.0)
plt.plot(data_file['time'],data_file['np'],'ro')
plt.legend(['Predicted','Measured'])
plt.ylabel('Moles')

ax = plt.subplot(3,1,2)
plt.plot(y['time'],y['x[1]'],'bx-',linewidth=2.0)
plt.plot(data_file['time'],data_file['x[1]'],'ro')
plt.plot(y['time'],y['xp'],'k:',linewidth=2.0)
plt.legend(['Predicted','Measured','Cumulative'])
plt.ylabel('Composition')
ax.set_ylim([0.6, 1.05])

plt.subplot(3,1,3)
plt.plot(y['time'],y['x[1]'],'bx-',linewidth=2.0)
plt.plot(y['time'],y['x[2]'],'k:',linewidth=2.0)
plt.plot(y['time'],y['x[5]'],'r--',linewidth=2.0)
plt.plot(y['time'],y['x[10]'],'m.-',linewidth=2.0)
plt.plot(y['time'],y['x[20]'],'y-',linewidth=2.0)
plt.plot(y['time'],y['x[30]'],'g-.',linewidth=2.0)
plt.plot(y['time'],y['x[40]'],'k-',linewidth=2.0)
plt.legend(['x1','x2','x5','x10','x20','x30','x40'])
plt.ylabel('Composition')

plt.savefig('results_l1.png')
plt.show()
