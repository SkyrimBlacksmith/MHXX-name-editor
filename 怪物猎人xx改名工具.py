#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys;

def check():
	name = sys.argv[3];
	if len(sys.argv) != 4:
		print('Parameters are error');
		sys.exit();
	if len(name) > 12:
		print('Player name is illegal');
		sys.exit();
	elif len(name) == 0:
		print('Player name cannot be empty');
		sys.exit();

check();

path = sys.argv[1];
slot = int(sys.argv[2]);
name = sys.argv[3];

original_offset = 0x126474;
display_offset = 0x23B7D;
guild_offset = 0xC71BD;
slot_offset = 0x11E7C0;

present_offest = original_offset + slot_offset * (slot - 1);

fill = b'\x00';
fill_len = 12 - len(name);
name_8 = name.encode('utf-8') + fill * fill_len;
name_16 = name.encode('utf-16le') + fill * fill_len;

file = open(path, mode = 'rb+');

file.seek(present_offest);
file.write(name_8);

file.seek(present_offest + display_offset);
file.write(name_8);

file.seek(present_offest + guild_offset);
file.write(name_16);

file.close();
print('Complete!');