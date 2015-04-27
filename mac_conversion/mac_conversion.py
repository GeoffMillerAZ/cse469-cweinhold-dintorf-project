#############################
#							#
#	mac_conversion.py		#
#	@author Dylan Intorf	#
#							#
#############################

import optparse
import binascii
import struct
import datetime

global p
p = optparse.OptionParser()

def main():
	# add options to OptionParser
	p.add_option('-T', action='store_true', help='Use the time conversion module. Either -f or -h must be given.')
	p.add_option('-D', action='store_true', help='Use the date conversion module. Either -f or -h must be given.')
	p.add_option('-f', dest='filename', metavar='filename', action='store', help='This specifies the path to a filename that includes a hex value of time or date. Note that the hex value should follow this notation: 0x1234. For the multiple hex values in either a file or a command line input, we consider only one hex value so the recursive mode for MAC conversion is optional.')
	p.add_option('-x', dest='hex_value', metavar='hex value', action='store', help='This specifies the hex value for converting to either date or time value. Note that the hex value should follow this notation: Ox1234. For the multiple hex values in either a file or acommand line input, we consider only one hex value so the recursive mode for MAC conversion is optional.')
	
	# get options from parser
	options, arguments = p.parse_args()

	# if -T option given
	if options.T:
		# if -f option given
		if options.filename:
			try:
				# open file and get each hex value
				with open(options.filename,"r") as inf:
					# loop through lines
					for line in inf:
						# strip extra spacing
						value = line.strip()
						# print result from convert_time
						print "Time: %s" % convert_time(value)
			except Exception as e:
				# print Exception
				print "ERROR: %s" % str(e)
		# if -x option given
		elif options.hex_value:
			# print result from convert_time
			print "Time: %s" % convert_time(options.hex_value)
		else:
			# options not given ERROR
			print "ERROR: You must specify a filename or a hex value."
			p.print_help()
	# if -D option given
	elif options.D:
		# if -f option given
		if options.filename:
			try:
				# open file and get each hex value
				with open(options.filename,"r") as inf:
					# loop through lines
					for line in inf:
						# strip extra spacing
						value = line.strip()
						# print result from convert_date
						print "Date: %s" % convert_date(value)
			except Exception as e:
				# print Exception
				print "EXCEPTION ERROR: %s" % str(e)
		# if -x option given
		elif options.hex_value:
			# print result from convert_date
			print "Date: %s" % convert_date(options.hex_value)
		else:
			# options not given ERROR
			print "ERROR: You must specify a filename or a hex value."
			p.print_help()
	else:
		# options not given ERROR
		print "ERROR: No valid options given. You must specify -T or -D."
		p.print_help()

# function to convert hex to date
def convert_date(hex):
	if len(hex) > 6:
		return "ERROR: Hex value is too long."
	# convert hex to little endian
	little_endian = "0x%04X" % struct.unpack("<H", binascii.unhexlify(hex[2:]))
	# convert little endian hex to binary
	binary = (bin(int(little_endian,16))[2:]).zfill(16)
	# get year, month, and day from binary
	year = int(binary[:7],2)
	month = int(binary[7:11],2)
	day = int(binary[11:],2)
	# create date from year, month, and day
	try:
		date = datetime.date(year+1980, month, day)
	except Exception as e:
		return "EXCEPTION ERROR: Hex could not be converted to date, %s" % str(e)
	# return date string
	return date.strftime('%b %d, %Y')

# function to convert hex to date
def convert_time(hex):
	if len(hex) > 6:
		return "ERROR: Hex value is too long."
	# convert hex to little endian
	little_endian = "0x%04X" % struct.unpack("<H", binascii.unhexlify(hex[2:]))
	# convert little endian hex to binary
	binary = (bin(int(little_endian,16))[2:]).zfill(16)
	# get hour, minutes, and seconds from binary
	hour = int(binary[:5],2)
	minute = int(binary[5:11],2)
	second = int(binary[11:],2)
	if second > 29:
		return "ERROR: Hex could not be converted to time, second must be in 0..29"
	second *= 2
	# create time from hour, minutes, and seconds
	try:
		time = datetime.time(hour,minute,second)
	except Exception as e:
		return "EXCEPTION ERROR: Hex could not be converted to time, %s" % str(e)
	# return time string
	return time.strftime('%I:%M:%S %p')

if __name__ == '__main__':
	main()