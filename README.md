# 北京联通IPTV播放列表（每日自动更新）

* `iptv-multicast.m3u`: 带有组播地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取
* `iptv-unicast.m3u`: 转换为单播地址的播放列表，需要使本地网络能解析 `udpxy.local` 域名到您可访问的 `udpxy` 实例，您也可以将文件中的 `udpxy.local` 替换为您可访问的 `udpxy` 实例地址
* `epg.xml`: 节目指南数据，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer epg.py](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/blob/main/epg.py) 抓取
* `epg.xml.gz`: 上面那个文件的压缩版，节目单中自动调用此文件
