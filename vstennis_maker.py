#!/usr/bin/python
import shutil
import sys
import glob

file_map = {'1a': ['mds-te a-2.1a', 'mds-te a-2.6a'],
            '1b': ['mds-te a-2.1b', 'mds-te a-2.6b'],
            '1c': ['mds-te a-2.1c', 'mds-te a-2.6c'],
            '1d': ['mds-te a-3.1d','mds-te a-3.6d'],
            '2a': ['mds-te a.2a', 'mds-te a.8a'],
            '2b': ['mds-te a.2b', 'mds-te a.8b']}
def main(argv):
  if len(argv) != 2:
    print "Usage: ./vstennis_maker <directory>"
    print "Directory will be renamed to vstennis to be moved to a MAME ROM directory"
    print "Add an rp2c0x.pal file to the directory for the game to work."
    sys.exit(-1)
  for source in file_map:
    sources = glob.glob("%s/*.%s" %(argv[1], source))
    for output in file_map[source]:
      outfile = "%s/%s" % (argv[1], output)
      if len(sources) == 0:
        fh = open(outfile, 'w')
        block = '00'.decode('hex') * 8192
        fh.write(block)
        fh.close()
      else:
        shutil.copy(sources[0], outfile)

if __name__ == '__main__':
  main(sys.argv)