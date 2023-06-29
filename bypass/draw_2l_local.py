from brian2 import *
import pickle
from scipy.signal import savgol_filter
from matplotlib.pyplot import figure
from matplotlib.pyplot import cm

def draw_spikes(file_name, plot_id, render_start, render_duration, y_lim, color_scheme):
  with open(file_name, 'rb') as m_f:
    m_mon = pickle.load(m_f)
    subplot(plot_id)
    plot(m_mon["t"]/second, m_mon['i'], color_scheme)
    xlim([render_start/second, render_duration/second])
    ylim([-0.5, y_lim])
    return True
  return False

step_duration = 1*second

cut_fibers_num = 100 ##24
muscle_fibers_num = 100 ##8
rg_num = 200 ## 48 # 200
motor_num = 200 ##48 # 200
V3_F_num = 100
bs_num = 100

total_save_seconds=2
# load_path_prefix = './out/2023-06-16_2l_5s_2nd_run/'
# load_path_prefix = './out/2023-06-19_2l_5s_InF_InE_run/'
# load_path_prefix = './out/2023-06-19_2l_5s_InF_InE_bs_run/'
# load_path_prefix = './out/2023-06-19_2l_5s_InF_InE_bs_2nd_run/'
load_path_prefix = '../../bypass/out/long_run/'

dirs = list(range(60, total_save_seconds+60, 60))
file_name = 'cut2rg_weigts.pickle'
print(dirs)

# Left leg
## Exetensor
steps_num = 1
render_start = step_duration * 0.0 * ms
render_duration = (step_duration*steps_num) * second
render_dirs = list(range(60, steps_num+60, 60))

figure(figsize=(20, 30))
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  c_file_name = 'l_e_cut_spikes.pickle'
  draw_spikes(load_path + c_file_name, 511, render_start, render_duration, cut_fibers_num, "r,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'l_e_muscle_spikes.pickle'
  draw_spikes(load_path + m_file_name, 512, render_start, render_duration, muscle_fibers_num, "r,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  c_file_name = 'l_e_bs_spikes.pickle'
  draw_spikes(load_path + c_file_name, 513, render_start, render_duration, bs_num, "k,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  r_file_name = 'l_e_rg_neurons_spikes.pickle'
  draw_spikes(load_path + r_file_name, 514, render_start, render_duration, rg_num, "g,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  motor_file_name = 'l_e_motor_neurons_spikes.pickle'
  draw_spikes(load_path + motor_file_name, 515, render_start, render_duration, motor_num, "m,")
show()

# Left leg
## Flexor
# Input singnals
steps_num = 60
render_start = step_duration * 0.0 * ms
render_duration = (step_duration * steps_num) * second
render_dirs = list(range(60, steps_num + 60, 60))

figure(figsize=(20, 30))

for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'l_f_muscle_spikes.pickle'
  draw_spikes(load_path + m_file_name, 611, render_start, render_duration, muscle_fibers_num, "r,")

for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'l_f_V3_F_spikes.pickle'
  draw_spikes(load_path + m_file_name, 612, render_start, render_duration, V3_F_num, "r,")

for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'l_f_bs_spikes.pickle'
  draw_spikes(load_path + m_file_name, 613, render_start, render_duration, bs_num, "k,")

for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  c_file_name = 'l_f_Ia_spikes.pickle'
  draw_spikes(load_path + c_file_name, 614, render_start, render_duration, cut_fibers_num, "b,")

for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  r_file_name = 'l_f_rg_neurons_spikes.pickle'
  draw_spikes(load_path + r_file_name, 615, render_start, render_duration, rg_num, "g,")

for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  motor_file_name = 'l_f_motor_neurons_spikes.pickle'
  draw_spikes(load_path + motor_file_name, 616, render_start, render_duration, motor_num, "m,")
show()

# Right leg
## Extensor
steps_num = 60
render_start = step_duration * 0.0 * ms
render_duration = (step_duration * steps_num) * second
render_dirs = list(range(60, steps_num + 60, 60))

# Input singnals
figure(figsize=(20, 30))
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  c_file_name = 'r_e_cut_spikes.pickle'
  draw_spikes(load_path + c_file_name, 611, render_start, render_duration, cut_fibers_num, "r,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'r_e_muscle_spikes.pickle'
  draw_spikes(load_path + m_file_name, 612, render_start, render_duration, muscle_fibers_num, "r,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  c_file_name = 'r_e_Ia_spikes.pickle'
  draw_spikes(load_path + c_file_name, 613, render_start, render_duration, cut_fibers_num, "b,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'r_e_bs_spikes.pickle'
  draw_spikes(load_path + m_file_name, 614, render_start, render_duration, bs_num, "k,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  r_file_name = 'r_e_rg_neurons_spikes.pickle'
  draw_spikes(load_path + r_file_name, 615, render_start, render_duration, rg_num, "g,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  motor_file_name = 'r_e_motor_neurons_spikes.pickle'
  draw_spikes(load_path + motor_file_name, 616, render_start, render_duration, motor_num, "m,")
show()
# Right leg
## Flexor
# Input singnals
steps_num = 60
render_start = step_duration * 0.0 * ms
render_duration = (step_duration * steps_num) * second
render_dirs = list(range(60, steps_num + 60, 60))
figure(figsize=(20, 30))
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'r_f_muscle_spikes.pickle'
  draw_spikes(load_path + m_file_name, 611, render_start, render_duration, muscle_fibers_num, "r,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'r_f_V3_F_spikes.pickle'
  draw_spikes(load_path + m_file_name, 612, render_start, render_duration, V3_F_num, "r,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  c_file_name = 'r_f_Ia_spikes.pickle'
  draw_spikes(load_path + c_file_name, 613, render_start, render_duration, cut_fibers_num, "b,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  m_file_name = 'r_f_bs_spikes.pickle'
  draw_spikes(load_path + m_file_name, 614, render_start, render_duration, bs_num, "k,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  r_file_name = 'r_f_rg_neurons_spikes.pickle'
  draw_spikes(load_path + r_file_name, 615, render_start, render_duration, rg_num, "g,")
for d in render_dirs:
  load_path = load_path_prefix + str(d) + '/'
  motor_file_name = 'r_f_motor_neurons_spikes.pickle'
  draw_spikes(load_path + motor_file_name, 616, render_start, render_duration, motor_num, "m,")
show()

# Weights
## Left leg
### Extensor

figure(figsize=(20, 10))
file_name = 'l_e_cut2rg_weigts.pickle'
file_rg2InE = 'l_e_rg2InE_weigts.pickle'
# 60
load_path_60 = load_path_prefix + str(dirs[0]) + '/'
print(load_path_60)

with open(load_path_60 + file_name, 'rb') as f60:
  mon60 = pickle.load(f60)
  # subplot(411)
  # plot(mon60["t"], mon60['s'])
  # xlim([render_start/second, render_duration/second])

  ## avg
  avg_w = average(mon60['s'], axis=1)
  smoothed_avg_w = savgol_filter(avg_w, 31, 4)
  max_w = percentile(mon60['s'], 15, axis=1)
  min_w = percentile(mon60['s'], 85, axis=1)
  var_w = std(mon60['s'], axis=1)
  smoothed_var_w = savgol_filter(var_w, 31, 4)

  ## avg
  subplot(511)
  plot(mon60['t'] / second, smoothed_avg_w, 'tab:green')
  plot(mon60['t'] / second, max_w, 'tab:blue')
  plot(mon60['t'] / second, min_w, 'tab:orange')
  # xlim([render_start/second, render_duration/second])
  tight_layout()

  subplot(512)
  plot(mon60['t'] / second, var_w, 'tab:red')
  # xlim([render_start/second, render_duration/second])
  tight_layout()

  with open(load_path_60 + file_rg2InE, 'rb') as frg2InE:
    rg2InE = pickle.load(frg2InE)

    avg_w_rg2InE = average(rg2InE['s'], axis=1)
    smoothed_avg_w_avg_w_rg2InE = savgol_filter(avg_w_rg2InE, 21, 4)
    max_w = percentile(rg2InE['s'], 15, axis=1)
    min_w = percentile(rg2InE['s'], 85, axis=1)
    ## avg
    subplot(513)
    plot(rg2InE['t'] / second, smoothed_avg_w, 'tab:green')
    plot(rg2InE['t'] / second, max_w, 'tab:blue')
    plot(rg2InE['t'] / second, min_w, 'tab:orange')
    tight_layout()
show()
