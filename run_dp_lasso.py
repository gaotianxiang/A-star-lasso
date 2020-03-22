from dp_lasso import wrap_dp_lasso

net_id = 15
lambda_ = 0.3
lower_bd = 0.5
upper_bd = 1
set_ = 0
num_samples = 500
wrap_dp_lasso(net_id, num_samples, lower_bd, upper_bd, lambda_, set_)
