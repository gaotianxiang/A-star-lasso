Networks = ['tree', 'inversetree', 'factors', 'alarm', 'barley', 'carpo', 'chain',
            'hailfinder', 'insurance', 'mildew', 'water', 'vstructure', 'treebranch',
            'inversetreebranch', 'skinnytree', 'asia', 'dsep', 'bowling', 'funnel',
            'insurancesmall', 'alarm300', 'walrus', 'shallow21', 'chain20', 'rain',
            'cloud', 'galaxy', 'hailfinder300']


def gen_simu_data(net_id, num_sets, lower_bd, upper_bd, num_samples):
    name = Networks[net_id]



#
# addpath ./networks
# addpath ./utils
# % addpath ../SBN/Toolbox/Causal_Explorer/Matlab_R14;
# % addpath ../SBN/Toolbox/Causal_Explorer/Matlab_R14/Pcodes;
# n = 2500; %number of samples
#
# name = Networks{netid};
# netFunc = str2func(strcat('getDAG',name));
# [Ayy,nodeNames,toporder] = netFunc(); %A for adjacency
# q = length(nodeNames);
#
# dirname = './simdata';
# for i = 1:q
#     nodeNums{i} = int2str(i);
# end
#
# %Use this if you want to visualize the network
# plotNetwork(Ayy,nodeNums,dirname,name)
#
# disp(sprintf('Generating Data for Network %s.', name));
# for i = 1:nsets
#     msg = sprintf('Generating set %d.', i);
#     disp(msg);
#     filename = sprintf('%s/%s/%s_lb%dub%d_set%d.mat', dirname,name,name,lowerbd*10, upperbd*10,i);
#     [Y, betatrue] = forwardSample(Ayy,toporder,n,q,lowerbd,upperbd);
#     save(filename, 'Y', 'Ayy', 'toporder', 'name', 'lowerbd', 'upperbd', 'betatrue') ;
#     clear Y;
#     clear betatrue;
# end
#
# end
