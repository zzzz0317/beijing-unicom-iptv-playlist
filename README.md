# 北京联通IPTV播放列表（每日自动更新）

* [iptv-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-multicast.m3u): 带有组播地址的播放列表，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/) 抓取
* [iptv-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-unicast.m3u): 转换为单播地址的播放列表，需要使本地网络能解析 `udpxy.local` 域名到您可访问的 `udpxy` 实例，您也可以将文件中的 `udpxy.local` 替换为您可访问的 `udpxy` 实例地址
* [epg.xml](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml): 节目指南数据，通过 [zzzz0317/beijing-unicom-iptv-playlist-sniffer epg.py](https://github.com/zzzz0317/beijing-unicom-iptv-playlist-sniffer/blob/main/epg.py) 抓取
* [epg.xml.gz](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/epg.xml.gz): 上面那个文件的压缩版，节目单中自动调用此文件
* [rawplaylist.json](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/rawplaylist.json): 原始节目单
* [iptv-ignored-multicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-multicast.m3u): 无法播放频道的播放列表(组播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)
* [iptv-ignored-unicast.m3u](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/raw/refs/heads/main/iptv-ignored-unicast.m3u): 无法播放频道的播放列表(单播)，若您发现其中的频道可以播放，请提交 [Issue](https://github.com/zzzz0317/beijing-unicom-iptv-playlist/issues/)

## 播放列表转换工具 convert.py

适用于自部署 Web 服务的情况，以下示例假设您的服务器 IP 地址为 10.1.1.1，并且在该服务器上安装了 udpxy 和 Nginx

转换: `./convert.py --rtp-url http://10.1.1.1:8081/rtp/ --epg-url http://10.1.1.1:8081/epg.xml.gz --logo-url http://10.1.1.1:8081/img/ --output iptv.m3u`

然后将整个目录使用 Nginx 等工具承载即可，以下是一个示例的 Nginx 虚拟主机配置文件

```
server {
    listen 8081;
    #server_name 10.1.1.1;
    root /var/www/iptv;

    location /rtp {
        proxy_redirect off;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_pass http://127.0.0.1:8080;
    }
}
```

配置仅供参考，请按实际情况修改，并且将更新仓库和转换的命令放在crontab中定时执行。
