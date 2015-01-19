# NESToVsRoms
Script to extract 8KB ROMs from iNES format Nintendo Entertainment System ROM files.

# Usage
./nes_to_vs_rom.py <yourgame.nes> <output_directory>

The script will generate a ROM set with the filename: yourgame.1[a-d] and yourgame.2[a-b]. These ROMs can then be burned to EPROMs and potentially used on Nintendo Versus hardware.

# Identification Compatible Games
Games with 16K PRG and 8K of CHR should fit. Theoretically 32k PRG / 16k CHR should fit.

# Known Working Games
