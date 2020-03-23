import argparse

from a_star_lasso import wrap_astar_lasso

parser = argparse.ArgumentParser()
parser.add_argument('--netid', default=15, type=int)
parser.add_argument('--lambda_', '--l', default=0.2, type=float)
parser.add_argument('--lower_bd', '--lbd', default=0.5, type=float)
parser.add_argument('--upper_bd', '--ubp', default=1, type=float)
parser.add_argument('--set_', default=1, type=int)
parser.add_argument('--num_samples', '--n', default=500, type=int)

args = parser.parse_args()
wrap_astar_lasso(args.netid, args.num_samples, args.lower_bd, args.upper_bd, args.lambda_, args.set_)
