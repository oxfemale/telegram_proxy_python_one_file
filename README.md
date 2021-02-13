# Async MTProto Proxy #

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