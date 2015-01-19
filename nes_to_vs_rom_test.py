#!/opt/local/bin/python2.7

import nes_to_vs_rom
import unittest
import StringIO

class NesToVsRomTest(unittest.TestCase):

  def testCanLoadHeader(self):
    nes = nes_to_vs_rom.NESFormatReader('NEStress.NES')
    nes.ParseFile()
    self.assertEqual(2, nes.headers.prg_16k_blocks)
    self.assertEqual(1, nes.headers.chr_blocks)

  def testHasTrainer(self):
    nes = nes_to_vs_rom.NESFormatReader('NEStress.NES')
    no_trainer_header = "4E45531A020101000000000000000000".decode('hex')
    nes.ParseHeader(no_trainer_header)
    trainer_header = "4E45531A020105000000000000000000".decode('hex')
    nes = nes_to_vs_rom.NESFormatReader('NEStress.NES')
    nes.ParseHeader(trainer_header)
    self.assertTrue(nes.hasTrainer())

  def testGetMapperType(self):
    nes = nes_to_vs_rom.NESFormatReader('NEStress.NES')
    header = "4E45531A101040000000000000000000".decode('hex')
    nes.ParseHeader(header)
    self.assertEqual(4, nes.getMapperType())

  def testGetPrgBlock(self):
    expected = open('prg_1_chunk').read()
    nes = nes_to_vs_rom.NESFormatReader('NEStress.NES')
    nes.ParseFile()
    self.assertEqual(expected, nes.GetPrgBlock(1))

  def testGetChrBlock(self):
    expected = open('chr_1_chunk').read()
    nes = nes_to_vs_rom.NESFormatReader('NEStress.NES')
    nes.ParseFile()
    self.assertEqual(expected, nes.GetChrBlock(1))

if __name__ == '__main__':
  unittest.main()