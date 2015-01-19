# NESToVsRoms
Script to extract 8KB ROMs from iNES format Nintendo Entertainment System ROM files.

# Usage
./nes_to_vs_rom.py <yourgame.nes> <output_directory>

The script will generate a ROM set with the filename: yourgame.1[a-d] and yourgame.2[a-b]. These ROMs can then be burned to EPROMs and potentially used on Nintendo Versus hardware.

# Identification Compatible Games
Games with 16K PRG and 8K of CHR should fit. Theoretically 32k PRG / 16k CHR should fit.

# Testing games without burning EPROMs
Included here is the _vstennis_maker.py_ script which will take a resulting output directory from nes_to_vs_rom.py and create files which look like a vstennis MAME romset.

The directory can then be renamed to vstennis be copied to your mame roms directory. For the game to work you'll need to add an rp2c0x.pal file from another Vs. game like duckhunt.

Once this is complete the game can be tested by running mame for the vstennis game. It will complain about CRC mismatches and warn you but the game should work.
# Known Working Games
