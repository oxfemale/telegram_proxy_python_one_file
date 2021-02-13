PORT = 55000
SOCKS5_HOST = "localhost"
SOCKS5_PORT = 9050

# name -> secret (32 hex chars)
USERS = {
    "lulz" : "0000000000000000000000000000000",
    "ecor" : "00000000000000000000000000000000"
}


USER_MAX_TCP_CONNS = {  }
#TLS_DOMAIN = "www.google.com"

MODES = { "classic": True, "secure": False, "tls": True }

# The domain for TLS mode, bad clients are proxied there
# Use random existing domain, proxy checks it on start
# TLS_DOMAIN = "www.google.com"

# Tag for advertising, obtainable from @MTProxybot
# AD_TAG = "3c09c680b76ee91a4c25ad51f742267d"
