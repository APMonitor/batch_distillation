# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:16:57 2019

@author: brancox
"""

from apm import *

s = 'http://byu.apmonitor.com'
a = 'distill_sq_error'

apm(s,a,'clear all')
apm_load(s,a,'distill.apm')
csv_load(s,a,'data.csv')

apm_option(s,a,'nlc.imode',4)
apm_option(s,a,'nlc.max_iter',100)
apm_option(s,a,'nlc.nodes',2)
apm_option(s,a,'nlc.time_shift',0)
apm_option(s,a,'nlc.ev_type',2)

apm_info(s,a,'FV','hf')
apm_info(s,a,'FV','vf')
apm_info(s,a,'FV','tray_hol')
apm_info(s,a,'FV','condenser_hol')

apm_info(s,a,'CV','x[1]')
apm_info(s,a,'CV','np')

output = apm(s,a,'solve')
print(output)

y = apm_sol(s,a)

import matplotlib.pyplot as plt
import pandas as pd
#data_file = pd.read_csv('data_for_plotting.csv')

plt.figure(1,figsize=(12,8))
plt.subplot(3,1,1)
plt.plot(y['time'],y['np'],'bx-',linewidth=2.0)
#plt.plot(data_file['time'],data_file['np'],'ro')
plt.legend(['Predicted'])
plt.ylabel('Moles')

ax = plt.subplot(3,1,2)
plt.plot(y['time'],y['x[1]'],'bx-',linewidth=2.0)
#plt.plot(data_file['time'],data_file['x[1]'],'ro')
plt.plot(y['time'],y['xp'],'k:',linewidth=2.0)
plt.legend(['Predicted','Cumulative'])
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

plt.savefig('simulation.png')
plt.show()
