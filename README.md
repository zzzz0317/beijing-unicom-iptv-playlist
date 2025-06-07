# 北京联通IPTV播放列表（每日自动更新）

* [iptv-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-multicast.m3u): 带有组播地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取
* [iptv-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast.m3u): 转换为单播地址的播放列表，需要使本地网络能解析 `udpxy.local` 域名到您可访问的 `udpxy` 实例，您也可以将文件中的 `udpxy.local` 替换为您可访问的 `udpxy` 实例地址
* [epg.xml](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml): 节目指南数据，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer epg.py](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/blob/main/epg.py) 抓取
* [epg.xml.gz](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml.gz): 上面那个文件的压缩版，节目单中自动调用此文件
* [rawplaylist.json](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/rawplaylist.json): 原始节目单
* [iptv-ignored-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-multicast.m3u): 无法播放频道的播放列表(组播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
* [iptv-ignored-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-unicast.m3u): 无法播放频道的播放列表(单播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
