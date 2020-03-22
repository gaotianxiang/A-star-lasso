import numpy as np
import os
import pickle

from dp_lasso import dp_lasso

Networks = ['tree', 'inversetree', 'factors', 'alarm', 'barley', 'carpo', 'chain',
            'hailfinder', 'insurance', 'mildew', 'water', 'vstructure', 'treebranch',
            'inversetreebranch', 'skinnytree', 'asia', 'dsep', 'bowling', 'funnel',
            'insurancesmall', 'alarm300', 'walrus', 'shallow21', 'chain20', 'rain',
            'cloud', 'galaxy', 'hailfinder300']


def wrap_dp_lasso(net_id, num_samples, lower_bd, upper_bd, lambda_, set_):
    name = Networks[net_id]
    file_name = os.path.join('./simdata', name,
                             '{}_lb{}_ub{}_set{}.pkl'.format(name, lower_bd * 10, upper_bd * 10, set_))
    with open(file_name, 'rb') as file:
        data = pickle.load(file)

    # standardize
    y_complete = data['Y']
    y_train = y_complete[:num_samples, :]
    num, dim = np.shape(y_train)
    mean_y = np.mean(y_train, axis=0)
    y_train -= mean_y

    # validation set
    y_val = y_complete[num_samples: num_samples + 500, :]
    y_val -= y_val - mean_y

    # test set
    y_test = y_complete[num_samples + 500:, :]
    y_test -= mean_y

    solution = dp_lasso(y_train, lambda_)
    adj_matrix = solution.adj_matrix
    print(adj_matrix)




# function
# wrapDPLasso(netid, nsamples, lowerbd, upperbd, lambda , set)
# tic
# ct = cputime;
# [solution] = DPLasso(Y, lambda , 'lasso', 'matlab');
# elcputime = cputime - ct;
# toc
# time = toc;
# ZZ = solution.Z;
# Beta_ls = zeros(q);
# Beta_ls = getBetaLeastSq(Beta_ls, Y, ZZ);
# valerr = sqrt(sum(sum((YYval - YYval * Beta_ls). ^ 2)) / m);
# testerror = sqrt(sum(sum((YYtest - YYtest * Beta_ls). ^ 2)) / k);
#
# % result.queue = queue;
# result.meany = meany;
# result.trueZ = trueZ;
# result.valerr = valerr;
# result.solution = solution;
# result.
# lambda = lambda;
#        result.Beta_ls = Beta_ls;
#        result.testerr = testerror;
#        result.time = time;
#        result.elcputime = elcputime;
#
#        h = figure(1);
#        colormap('default');
#        subplot(2, 1, 1);
#        imagesc(trueZ);
#        title('Truth');
#        subplot(2, 1, 2);
#        imagesc(abs(result.Beta_ls));
#        title('Best Beta');
#
#        outdirname = './results_simulations';
#        outfilename = sprintf('%s/%s/%s_dp_%s_n%d_lb%dub%d_lambda%d_set%d.mat', outdirname, name, name, 'glmnet',
#        nsamples, lowerbd*10, upperbd * 10, lambda , set);
# save(outfilename, 'result');
#
# end
