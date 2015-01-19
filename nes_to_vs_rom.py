#!/opt/local/bin/python2.7

"""iNES format ROM to VS ROM files converter.

The resulting ROM files are potentially compatible on Nintendo Vs. hardware.
"""
__author__ = "Dan Van Derveer<dan@van.derveer.com>"
import collections
import sys
import os.path

class NESFormatReader(object):
  """iNES Format reader.

  This parser is incomplete in its handling of flags."""
  def __init__(self, filename=None, handle=None):
    if handle:
      self.fh = handle
    else:
      self.fh = open(filename, 'r')
    self.headers = collections.namedtuple(
        'Headers', ['prg_16k_blocks', 'chr_blocks',
                    'flag_6_byte', 'flag_7_byte',
                    'prg_8k_blocks', 'flag_9_byte',
                    'flag_10_byte'])

  def ParseFile(self):
    self.ParseHeader(self.fh.read(16))

  def hasTrainer(self):
    return (self.headers.flag_6_byte & 4) == 4

  def getMapperType(self):
    mapper = (self.headers.flag_6_byte & 240) >> 4
    mapper += self.headers.flag_7_byte & 240
    return mapper

  def ParseHeader(self, header_bytes):
    header_position = 0
    for b in [0x4e, 0x45, 0x53, 0x1a]:
      if ord(header_bytes[header_position]) != b:
        raise Exception('Bad header')
      header_position += 1
    for a in ['prg_16k_blocks', 'chr_blocks', 'flag_6_byte', 'flag_7_byte',
              'prg_8k_blocks', 'flag_9_byte', 'flag_10_byte']:
      setattr(self.headers, a, ord(header_bytes[header_position]))
      header_position += 1

  def GetChrBlock(self, block_no):
    if block_no > self.headers.chr_blocks:
      raise IndexError("Invalid Chr index")
    self.fh.seek(0)
    offset = 16 + (self.headers.prg_16k_blocks * 16384) + ((block_no - 1) * 8192)
    if self.hasTrainer():
      offset += 512
    self.fh.seek(offset)
    return self.fh.read(8192)

  def GetPrgBlock(self, block_no):
    if block_no > self.headers.prg_16k_blocks:
      raise IndexError("Invalid Prg index")
    self.fh.seek(0)
    offset = 16 + ((block_no - 1) * 16384)
    if self.hasTrainer():
      offset += 512
    self.fh.seek(offset)
    return self.fh.read(16384)


def VerifyCompatibility(reader):
  print "This script does not yet verify if the ROM specifed will be compatible with Vs. hardware"


def WriteChunk(filename, data):
  if len(data) != 8192:
    raise Exception("Data not the right size: %s != 8192" % len(data))
  print "Writing %s" % filename
  fh = open(filename, 'w')
  fh.write(data)
  fh.close()


def ExtractChr(reader, output_name_base):
  for i in xrange(1, reader.headers.chr_blocks+1):
    filename = "%s%s" % (output_name_base, chr(99 - i))
    chunk = reader.GetChrBlock(i)
    WriteChunk(filename, chunk)


def ExtractPrg(reader, output_name_base):
  postfixes = ['b', 'a', 'd', 'c']
  filepostfix = 0
  for i in xrange(1, reader.headers.prg_16k_blocks+1):
    chunk = reader.GetPrgBlock(i)
    for y in xrange(0,2):
      filename = "%s%s" % (output_name_base, postfixes[filepostfix])
      WriteChunk(filename, chunk[y*8192:(y+1)*8192])
      filepostfix += 1


def main(argv):
  if len(argv) < 3:
    print "Invalid arguments. Example: ./nes_to_vs_rom.py my_rom.nes output_dir"
    sys.exit(-1)
  reader = NESFormatReader(argv[1])
  reader.ParseFile()
  VerifyCompatibility(reader)
  rom_name = os.path.basename(argv[1])
  ExtractChr(reader, "%s/%s.2" % (argv[2], rom_name))
  ExtractPrg(reader, "%s/%s.1" % (argv[2], rom_name))
  print "Done"


if __name__ == '__main__':
  main(sys.argv)