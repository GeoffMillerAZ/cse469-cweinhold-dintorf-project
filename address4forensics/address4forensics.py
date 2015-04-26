#############################
#							#
#	address4forensics.py	#
#	@author Dylan Intorf	#
#							#
#############################

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
	p.add_option('--byte-address', '-B', dest='get_b_addr', action='store_true', help='Instead of returning sector values for the conversion, this returns the byte address of the calculated value, which is the number of sectors multiplied by the number of bytes per sector.')
	p.add_option('--sector-size', '-s', default=512, dest='bytes', metavar=color.UNDERLINE + 'bytes' + color.END, action='store', help='When the -B option is used, this allows for a specification of ' + color.UNDERLINE + 'bytes' + color.END + ' per sector other than the default 512. Has no effect on output without -B.', type='int')
	p.add_option('--logical-known', '-l', dest='l_addr', metavar=color.UNDERLINE + 'address' + color.END, action='store', help='This specifies the known logical ' + color.UNDERLINE + 'address' + color.END + ' for calculating either a cluster address or a physical address. When used with the -L option, this simply returns the value given for ' + color.UNDERLINE + 'address' + color.END + '.', type='int')
	p.add_option('--physical-known', '-p', dest='p_addr', metavar=color.UNDERLINE + 'address' + color.END, action='store', help='This specifies the known physical ' + color.UNDERLINE + 'address' + color.END + ' for calculating either a cluster address or a logical address. When used with the -P option, this simply returns the value given for ' + color.UNDERLINE + 'address' + color.END + '.', type='int')
	p.add_option('--cluster-known', '-c', dest='c_addr', metavar=color.UNDERLINE + 'address' + color.END, action='store', help='This specifies the known cluster ' + color.UNDERLINE + 'address' + color.END + ' for calculating either a logical address or a physical address. When used with the -C option, this simply returns the value given for ' + color.UNDERLINE + 'address' + color.END + '. Note that options -k, -r, -t, and -f must be provided with this option.', type='int')
	p.add_option('--cluster-size', '-k', dest='cluster_size', metavar=color.UNDERLINE + 'sectors' + color.END, action='store', help='This specifies the number of ' + color.UNDERLINE + 'sectors' + color.END + ' per cluster.', type='int')
	p.add_option('--reserved', '-r', dest='reserved_sectors', metavar=color.UNDERLINE + 'sectors' + color.END, action='store', help='This specifies the number of reserved ' + color.UNDERLINE + 'sectors' + color.END + ' in the partition', type='int')
	p.add_option('--fat-tables', '-t', dest='tables', metavar=color.UNDERLINE + 'tables' + color.END, default=2, action='store', help='This specifies the number of FAT ' + color.UNDERLINE + 'tables' + color.END + ', which is usually 2', type='int')
	p.add_option('--fat-length', '-f', dest='fat_size', metavar=color.UNDERLINE + 'sectors' + color.END, action='store', help='This specifies the length of each FAT table in ' + color.UNDERLINE + 'sectors' + color.END, type='int')
	options, arguments = p.parse_args()

	try:
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
			p.print_help()
	except Exception as e:
		print "EXCEPTION ERROR: %s" % str(e)

# function to calculate logical address
def calc_logical(options):
	# if -l option, print address given
	if options.l_addr:
		return options.l_addr
	# if -c given
	elif options.c_addr:
		# if all cluster options given
		if hasClusterOptions(options):
			c_addr = options.c_addr
			cluster_size = options.cluster_size
			reserved_sectors = options.reserved_sectors
			tables = options.tables
			fat_size = options.fat_size
			if options.get_b_addr:
				bytes_per_sector = options.bytes
				return (reserved_sectors + tables*fat_size + (c_addr-2)*cluster_size) * bytes_per_sector
			return reserved_sectors + tables*fat_size + (c_addr-2)*cluster_size
		else:
			print "ERROR: Options -k, -r, -t, and -f must be specified with option -c."
			p.print_help()
			return ""
	# if -p given
	elif options.p_addr:
		p_addr = options.p_addr
		offset = options.offset
		if options.get_b_addr:
			bytes_per_sector = options.bytes
			return (p_addr - offset) * bytes_per_sector
		return p_addr - offset
	# options not given
	else:
		print "ERROR: Options -c or -p must be specified with option -L."
		p.print_help()
		return ""

# function to calculate physical address
def calc_physical(options):
	# if -p option, print address given
	if options.p_addr:
		return options.p_addr
	# if -c given
	elif options.c_addr:
		if hasClusterOptions(options):
			c_addr = options.c_addr
			offset = options.offset
			cluster_size = options.cluster_size
			reserved_sectors = options.reserved_sectors
			tables = options.tables
			fat_size = options.fat_size
			if options.get_b_addr:
				bytes_per_sector = options.bytes
				return (offset + reserved_sectors + tables*fat_size + (c_addr-2)*cluster_size) * bytes_per_sector
			return offset + reserved_sectors + tables*fat_size + (c_addr-2)*cluster_size
		else:
			print "ERROR: Options -k, -r, -t, and -f must be specified with option -c."
			p.print_help()
			return ""
	# if -p given
	elif options.l_addr:
		l_addr = options.l_addr
		offset = options.offset
		if options.get_b_addr:
			bytes_per_sector = options.bytes
			return (p_addr + offset) * bytes_per_sector
		return p_addr + offset
	# options not given
	else:
		print "ERROR: Options -c or -l must be specified with option -P."
		p.print_help()
		return ""

# function to calculate cluster address
def calc_cluster(options):
	# if -c option, print address given
	if options.c_addr:
		return options.c_addr
	# if -l given
	elif options.l_addr:
		if hasClusterOptions(options):
			l_addr = options.l_addr
			cluster_size = options.cluster_size
			reserved_sectors = options.reserved_sectors
			tables = options.tables
			fat_size = options.fat_size
			c_addr = ((l_addr - reserved_sectors - (tables*fat_size)) / cluster_size) + 2
		else:
			print "ERROR: Options -k, -r, -t, and -f must be specified to calculate cluster address."
			p.print_help()
			return ""
		if c_addr < 2:
			return "ERROR: Cluster addresses start at 2. Value returned %s." % str(c_addr)
		return c_addr
	# if -p given
	elif options.p_addr:
		if hasClusterOptions(options):
			p_addr = options.p_addr
			offset = options.offset
			cluster_size = options.cluster_size
			reserved_sectors = options.reserved_sectors
			tables = options.tables
			fat_size = options.fat_size
			c_addr = ((p_addr - offset - reserved_sectors - (tables*fat_size)) / cluster_size) + 2
		else:
			print "ERROR: Options -k, -r, -t, and -f must be specified to calculate cluster address."
			p.print_help()
			return ""
		if c_addr < 2:
			return "ERROR: Cluster addresses start at 2. Value returned %s." % str(c_addr)
		return c_addr
	# options not given
	else:
		print "ERROR: Options -l or -p must be specified with option -C."
		p.print_help()
		return ""

def hasClusterOptions(options):
	return options.cluster_size and options.reserved_sectors and options.fat_size

if __name__ == '__main__':
	main()