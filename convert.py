#!/usr/bin/python3
import os
import sys
import argparse

DIR_SCRIPT = os.path.dirname(os.path.realpath(sys.argv[0]))
DEFAULT_EPG = "https://raw.githubusercontent.com/zzzz0317/beijing-unicom-iptv-playlist/refs/heads/main/epg.xml.gz"
DEFAULT_LOGO = "https://raw.githubusercontent.com/zzzz0317/beijing-unicom-iptv-playlist/refs/heads/main/img/"

parser = argparse.ArgumentParser(description="播放列表转换工具")
parser.add_argument("--rtp-url", default="http://udpxy.local:8080/rtp/", help="eg: http://10.0.0.1:8080/rtp/")
parser.add_argument("--epg-url", default=DEFAULT_EPG, help="eg: https://raw.githubusercontent.com/zzzz0317/beijing-unicom-iptv-playlist/refs/heads/main/epg.xml.gz")
parser.add_argument("--logo-url", default=DEFAULT_LOGO, help="eg: https://raw.githubusercontent.com/zzzz0317/beijing-unicom-iptv-playlist/refs/heads/main/")
parser.add_argument("--output", default=os.path.join(DIR_SCRIPT, "iptv.m3u"), help="保存路径，默认为脚本目录的 iptv.m3u")
args = parser.parse_args()

with open(os.path.join(DIR_SCRIPT, "iptv-multicast.m3u"), "r", encoding="utf-8") as f_source_file:
    m3u_file = f_source_file.read()

m3u_file = m3u_file.replace(DEFAULT_EPG, args.epg_url)
m3u_file = m3u_file.replace(DEFAULT_LOGO, args.logo_url)
m3u_file = m3u_file.replace("rtp://", args.rtp_url)

#print(m3u_file)
with open(args.output, "w", encoding="utf-8") as f_target_file:
    f_target_file.write(m3u_file)
