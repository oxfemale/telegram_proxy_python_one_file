# Async MTProto Proxy #

One shot telegram proxy python file

On Debian/Ubuntu:
```bash
apt install git curl build-essential libssl-dev zlib1g-dev python3 pip3
```

2. Edit this basic service (especially paths and params):
```bash
mcedit /etc/systemd/system/mtprotoproxy.service

[Unit]
Description=mtprotoproxy
After=network.target
Conflicts=getty@tty1.service

[Service]
Type=simple
User=nobody
WorkingDirectory=/opt/mtprotoproxy
ExecStart=/usr/bin/python3 /opt/mtprotoproxy/mtprotoproxy.py /opt/mtprotoproxy/config.py
StandardInput=tty-force
StandardOutput=file:/opt/mtprotoproxy/mtprotoproxyOut.log

[Install]
WantedBy=multi-user.target

mtprotoproxy.service
systemctl daemon-reload
systemctl restart mtprotoproxy.service
systemctl status mtprotoproxy.service
systemctl stop mtprotoproxy.service
systemctl enable mtprotoproxy.service
```
