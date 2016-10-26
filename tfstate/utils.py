import os
import errno
import socket

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

# We call this to see if we are an AWS EC2 instance
# or on another machine (e.g. local).
def on_aws():
    ip = '169.254.169.254'
    timeout = 0.1
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((ip, 80))
        return True
    except Exception as e:
        print(e.message)
        return False

# This is used to "warm up" the AWS meta data API.
# We were seeing > 5 secs. on the first call after
# starting an instance. Successive calls were
# returned _much_ faster.
def ping_aws_meta_data_api():
    url = 'http://169.254.169.254/latest/meta-data/'
    try:
        urllib2.urlopen(url, timeout = 10)
    except Exception as e: print(e)