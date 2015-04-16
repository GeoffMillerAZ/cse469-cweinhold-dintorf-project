#!/usr/bin/env python
import optparse
import binascii
import struct
import datetime

def main():
	p = optparse.OptionParser()
	p.add_option('-T', action='store_true', help='Use the time conversion module. Either -f or -h must be given.')
	p.add_option('-D', action='store_true', help='Use the date conversion module. Either -f or -h must be given.')
	p.add_option('-f', dest='filename', metavar='filename', action='store', help='This specifies the path to a filename that includes a hex value of time or date. Note that the hex value should follow this notation: 0x1234. For the multiple hex values in either a file or a command line input, we consider only one hex value so the recursive mode for MAC conversion is optional.')
	p.add_option('-x', dest='hex_value', metavar='hex value', action='store', help='This specifies the hex value for converting to either date or time value. Note that the hex value should follow this notation: Ox1234. For the multiple hex values in either a file or acommand line input, we consider only one hex value so the recursive mode for MAC conversion is optional.')
	options, arguments = p.parse_args()

	if options.T:
		if options.filename:
			# open file get hex value
			# Convert given hex value to Time
			print "file"
		elif options.hex_value:
			# convert given hex value to Time
			convert_time(options.hex_value)
		else:
			print "ERROR"
	elif options.D:
		if options.filename:
			# open file get hex value
			# Convert given hex value to Time
			print "file"
		elif options.hex_value:
			# convert given hex value to Time
			convert_date(options.hex_value)
		else:
			print "ERROR"
	# num = "0x%04X" % struct.unpack("<H", binascii.unhexlify(options.hex_value[2:]))
	# print num
	# binary = (bin(int(num,16))[2:]).zfill(16)
	# print binary
	# year = binary[:7]
	# print int(year,2)
	# month = binary[7:11]
	# print int(month,2)
	# day = binary[11:]
	# print int(day,2)

def convert_date(hex):
	little_endian = "0x%04X" % struct.unpack("<H", binascii.unhexlify(hex[2:]))
	binary = (bin(int(little_endian,16))[2:]).zfill(16)
	year = int(binary[:7],2)
	month = int(binary[7:11],2)
	day = int(binary[11:],2)
	date = datetime.date(year+1980, month, day)
	print date.strftime('%B %d, %Y')
def convert_time(hex):
	print hex

if __name__ == '__main__':
	main()