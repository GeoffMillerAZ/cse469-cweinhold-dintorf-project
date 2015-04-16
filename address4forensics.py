#!/usr/bin/env python
import optparse

def main():
	p = optparse.OptionParser()
	p.add_option('--logical', '-L', action='store_true', help='Calculate the logical address from either the cluster address or the physical address. Either -c or -p must be given.')
	p.add_option('--physical', '-P', action='store_true', help='Calculate the physical address from either the cluster address or the logical address. Either -c or -l must be given.')
	p.add_option('--cluster', '-C', action='store_true', help='Calculate the cluster address from either the logical address or the physical address. Either -l or -p must be given.')
	p.add_option('--partition-start', '-b', default=0, dest='offset', metavar='offset', action='store', help='This specifies the physical address (sector number) of the start of the partition, and defaults to 0 for ease in working with images of a single partition. The offset value will always translate into logical address 0.', type='int')
	p.add_option('--byte-address', '-B', action='store_true', help='Instead of returning sector values for the conversion, this returns the byte address of the calculated value, which is the number of sectors multiplied by the number of bytes per sector.')
	p.add_option('--sector-size', '-s', dest='bytes', metavar='bytes', action='store', help='When the -B option is used, this allows for a specification of BYTES per sector other than the default 512. Has no effect on output without -B.', type='int')
	p.add_option('--logical-known', '-l', dest='l_addr', metavar='address', action='append', help='This specifies the known logical address for calculating either a cluster address or a physical address. When used with the -L option, this simply returns the value given for address', type='int')
	p.add_option('--physical-known', '-p', dest='p_addr', metavar='address', action='append', help='This specifies the known physical address for calculating either a cluster address or a logical address. When used with the -P option, this simply returns the value given for address.', type='int')
	p.add_option('--cluster-known', '-c', dest='c_addr', metavar='address', action='append', help='This specifies the known cluster address for calculating either a logical address or a physical address. When used with the -C option, this simply returns the value given for address. Note that options -k, -r, -t, and -f must be provided with this option.', type='int')
	p.add_option('--cluster-size', '-k', dest='cluster_size', metavar='sectors', action='append', help='This specifies the number of sectors per cluster.', type='int')
	p.add_option('--reserved', '-r', dest='reserved_sectors', metavar='sectors', action='append', help='This specifies the number of reserved sectors in the partition', type='int')
	p.add_option('--fat-tables', '-t', dest='tables', metavar='tables', default=2, action='store', help='This specifies the number of FAT TABLES, which is usually 2', type='int')
	p.add_option('--fat-length', '-f', dest='fat_size', metavar='sectors', action='append', help='This specifies the length of each FAT table in sectors', type='int')
	options, arguments = p.parse_args()

	print "Logical: %d" % options.l_addr[0]
	print "Physical: %d" % options.p_addr[0]

if __name__ == '__main__':
	main()