#!/usr/bin/env python
import optparse

# global option parser
global p
p = optparse.OptionParser()

# class for color text styles
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def main():
	# add options to OptionParser
	p.add_option('--logical', '-L', action='store_true', help='Calculate the logical address from either the cluster address or the physical address. Either -c or -p must be given.')
	p.add_option('--physical', '-P', action='store_true', help='Calculate the physical address from either the cluster address or the logical address. Either -c or -l must be given.')
	p.add_option('--cluster', '-C', action='store_true', help='Calculate the cluster address from either the logical address or the physical address. Either -l or -p must be given.')
	p.add_option('--partition-start', '-b', default=0, dest='offset', metavar=color.UNDERLINE + 'offset' + color.END, action='store', help='This specifies the physical address (sector number) of the start of the partition, and defaults to 0 for ease in working with images of a single partition. The ' + color.UNDERLINE + 'offset' + color.END + ' value will always translate into logical address 0.', type='int')
	p.add_option('--byte-address', '-B', action='store_true', help='Instead of returning sector values for the conversion, this returns the byte address of the calculated value, which is the number of sectors multiplied by the number of bytes per sector.')
	p.add_option('--sector-size', '-s', dest='bytes', metavar=color.UNDERLINE + 'bytes' + color.END, action='store', help='When the -B option is used, this allows for a specification of ' + color.UNDERLINE + 'bytes' + color.END + ' per sector other than the default 512. Has no effect on output without -B.', type='int')
	p.add_option('--logical-known', '-l', dest='l_addr', metavar=color.UNDERLINE + 'address' + color.END, action='append', help='This specifies the known logical ' + color.UNDERLINE + 'address' + color.END + ' for calculating either a cluster address or a physical address. When used with the -L option, this simply returns the value given for ' + color.UNDERLINE + 'address' + color.END + '.', type='int')
	p.add_option('--physical-known', '-p', dest='p_addr', metavar=color.UNDERLINE + 'address' + color.END, action='append', help='This specifies the known physical ' + color.UNDERLINE + 'address' + color.END + ' for calculating either a cluster address or a logical address. When used with the -P option, this simply returns the value given for ' + color.UNDERLINE + 'address' + color.END + '.', type='int')
	p.add_option('--cluster-known', '-c', dest='c_addr', metavar=color.UNDERLINE + 'address' + color.END, action='append', help='This specifies the known cluster ' + color.UNDERLINE + 'address' + color.END + ' for calculating either a logical address or a physical address. When used with the -C option, this simply returns the value given for ' + color.UNDERLINE + 'address' + color.END + '. Note that options -k, -r, -t, and -f must be provided with this option.', type='int')
	p.add_option('--cluster-size', '-k', dest='cluster_size', metavar=color.UNDERLINE + 'sectors' + color.END, action='append', help='This specifies the number of ' + color.UNDERLINE + 'sectors' + color.END + ' per cluster.', type='int')
	p.add_option('--reserved', '-r', dest='reserved_sectors', metavar=color.UNDERLINE + 'sectors' + color.END, action='append', help='This specifies the number of reserved ' + color.UNDERLINE + 'sectors' + color.END + ' in the partition', type='int')
	p.add_option('--fat-tables', '-t', dest='tables', metavar=color.UNDERLINE + 'tables' + color.END, default=2, action='store', help='This specifies the number of FAT ' + color.UNDERLINE + 'tables' + color.END + ', which is usually 2', type='int')
	p.add_option('--fat-length', '-f', dest='fat_size', metavar=color.UNDERLINE + 'sectors' + color.END, action='append', help='This specifies the length of each FAT table in ' + color.UNDERLINE + 'sectors' + color.END, type='int')
	options, arguments = p.parse_args()

	# if -L option given
	if options.logical:
		print calc_logical(options)
	# if -P option given
	elif options.physical:
		print calc_physical(options)
	# if -C option given
	elif options.cluster:
		print calc_cluster(options)
	# no valid options given
	else:
		print "ERROR: No valid options given. You must specify -L, -P, or -C."

# function to calculate logical address
def calc_logical(options):
	# if -l option, print address given
	if options.l_addr:
		return options.l_addr[0]
	# if -c given
	elif options.c_addr:
		print "Valid"
	# if -p given
	elif options.p_addr:
		print "Valid"
	# options not given
	else:
		print "ERROR: Options -c or -p must be specified with option -L."
		p.print_help()
		return ""
	return "calculating logical"

# function to calculate physical address
def calc_physical(options):
	# if -p option, print address given
	if options.p_addr:
		return options.p_addr[0]
	# if -c given
	elif options.c_addr:
		print "Valid"
	# if -p given
	elif options.l_addr:
		print "Valid"
	# options not given
	else:
		print "ERROR: Options -c or -l must be specified with option -L."
		p.print_help()
		return ""
	return "calculating physical"

# function to calculate cluster address
def calc_cluster(options):
	# if -c option, print address given
	if options.c_addr:
		return options.c_addr[0]
	# if -l given
	elif options.l_addr:
		print "Valid"
	# if -p given
	elif options.p_addr:
		print "Valid"
	# options not given
	else:
		print "ERROR: Options -l or -p must be specified with option -L."
		p.print_help()
		return ""
	return "calculating cluster"

if __name__ == '__main__':
	main()