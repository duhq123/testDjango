#!/usr/bin/env python
# -*- coding:utf8 -*-

from pydub import AudioSegment

enPath = "C:/Users/admin/Desktop/shy/1/1.mp3"           # 背景
cnPath = "C:/Users/admin/Desktop/shy/2/2.mp3"           # 样音
targetPath = "C:/Users/admin/Desktop/shy/3/5.mp3"       # 合并文档的路径

# 加载MP3文档
song1 = AudioSegment.from_mp3(enPath)                   # 加载背景
song2 = AudioSegment.from_mp3(cnPath)                   # 加载样音

# 取得两个MP3文档的声音分贝
db1 = song1.dBFS
db2 = song2.dBFS

# 调整两个MP3的声音大小，防止出现一个声音大一个声音小的情况
dbplus = db1 - db2
if dbplus < 0:                  # 判断如果背景声音小于样音的声音
    song1 += abs(dbplus)        # 将背景声音调整成样音声音的大小
elif dbplus > 0:                # 判断如果样音声音小于背景的声音
    song2 += abs(dbplus)        # 将样音声音调整成背景声音的大小


# 计算背景与样音合成的间隔时间
# 设置初始化间隔时长
ch_sh_h = 5000
kb_ai = AudioSegment.silent(duration=ch_sh_h)                   # 生成一个初始化间隔时间的空白音频
yang_y1 = song2 + kb_ai                                         # 将空白音频拼接到样音尾部
bj_shijian = len(song1)                                         # 获取背景时长
shy_shijian = len(yang_y1)                                      # 获取样音时长
x_h = bj_shijian / shy_shijian                                  # 背景时长除以样时长，等于循环次数
q_zh = int(x_h)                                                 # 循环次数如果是小数，只取整数
shy_shijian_q_zh = shy_shijian * q_zh                           # 样音时长乘以循环次数的整数，等于样循环之后的总时长
duo_yu = bj_shijian - shy_shijian_q_zh - ch_sh_h                # 背景时长减去，循环之后的总时长，在减去起始时长，等于循环之后多余的时长
f_t = duo_yu / q_zh                                             # 循环之后多余的时长除以循环次数的整数，等于多余的时长分摊给每次间隔的时长
z_zh = f_t + ch_sh_h                                            # 分摊的时长加上间隔的时长，等于最终间隔时长


# 根据计算后的间隔时间，重新生成空白音频拼接到样音
die_jia = song2 + AudioSegment.silent(duration=int(z_zh))
# 将重新计算生成的样音，叠加到背景上
played_togther = song1.overlay(die_jia, position=ch_sh_h, loop=True, gain_during_overlay=0)
print(played_togther)
"""
die_jia：保存路径
position：样音起始时间
loop：循环水印
gain_during_overlay：闪避音量
"""

# 导出为MP3格式
played_togther.export(
    targetPath,
    format="mp3",
    tags={"title": "标题", "artist": "专辑"},
    cover="C:/Users/admin/Desktop/shy/img/8868.jpg",
)