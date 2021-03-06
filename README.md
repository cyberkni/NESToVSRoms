# NESToVsRoms
Script to extract 8KB ROMs from iNES format Nintendo Entertainment System ROM files.

This currently is only supports games which do not require a daughterboard on the Dualsystem mainboard to run. However, it *is* possible to run NES games which require mappers with the right daughterboard. This is future work to be done.

# Usage
./nes_to_vs_rom.py <yourgame.nes> <output_directory>

The script will generate a ROM set with the filename: yourgame.1[a-d] and yourgame.2[a-b]. These ROMs can then be burned to EPROMs and potentially used on Nintendo Versus hardware.

# Identification Compatible Games
Games with 16K PRG and 8K of CHR should fit. Theoretically 32k PRG / 16k CHR should fit but has not been tested yet.

A good list of games/rom sizes/mappers can be found here: http://tuxnes.sourceforge.net/nesmapper.txt

# Testing games without burning EPROMs
Included here is the _vstennis_maker.py_ script which will take a resulting output directory from nes_to_vs_rom.py and create files which look like a vstennis MAME romset.

The directory can then be renamed to vstennis be copied to your mame roms directory. For the game to work you'll need to add an rp2c0x.pal file from another Vs. game like duckhunt.

Once this is complete the game can be tested by running mame for the vstennis game. It will complain about CRC mismatches and warn you but the game should work.

# Known Working Games
See the wiki [Game Compatibility List](https://github.com/cyberkni/NESToVSRoms/wiki/Game-Compatibility-List)
