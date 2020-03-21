#
# netid = 16; %for insurance network
# nsets = 10; %10 repetitions
# lowerbd = 0.5;  %lower bound on beta values
# upperbd = 1; %upper bound on beta values
# genSimuData(netid,nsets,lowerbd,upperbd)

from gen_simu_data import gen_simu_data

net_id = 15
num_sets = 1
lower_bd = 0.5
upper_bd = 1
num_samples = 2500
gen_simu_data(net_id, num_sets, lower_bd, upper_bd, num_samples)
