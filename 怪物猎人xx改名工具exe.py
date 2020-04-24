#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys;
from tkinter import *;
from tkinter import messagebox;

def check():
	if slot < 1 and slot >3:
		messagebox.showinfo('错误', '槽位输入错误');
		sys.exit();
	if len(name) > 12 or len(name) == 0:
		tmessagebox.showinfo('错误', '名字过长且名字不能为空');
		sys.exit();

Tk().withdraw();

path = input('输入存档路径(绝对路径和相对路径皆可)');
slot = int(input('输入存档栏位：'));
name = input('输入想要的名称：');

check();

original_offset = 0x126474;
display_offset = 0x23B7D;
guild_offset = 0xC71BD;
slot_offset = 0x11E7C0;

present_offest = original_offset + slot_offset * (slot - 1);

fill = b'\x00';
fill_len = 12 - len(name);
name_8 = name.encode('utf-8') + fill * fill_len;
name_16 = name.encode('utf-16le') + fill * fill_len;

try:
	file = open(path, mode = 'rb+');
except IOError:
	messagebox.showinfo('错误', '未找到该文件或读写该文件失败');
else:

	file.seek(present_offest);
	file.write(name_8);

	file.seek(present_offest + display_offset);
	file.write(name_8);

	file.seek(present_offest + guild_offset);
	file.write(name_16);

	file.close();
	messagebox.showinfo( '成功', '修改完成');