import argparse

from gen_simu_data import gen_simu_data

parser = argparse.ArgumentParser()
parser.add_argument('--netid', default=15, type=int)
parser.add_argument('--lower_bd', '--lbd', default=0.5, type=float)
parser.add_argument('--upper_bd', '--ubp', default=1, type=float)
parser.add_argument('--num_sets', default=10, type=int)
parser.add_argument('--num_samples', '--n', default=2500, type=int)

args = parser.parse_args()
gen_simu_data(args.netid, args.num_sets, args.lower_bd, args.upper_bd, args.num_samples)
