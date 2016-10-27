import os
import errno

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc: # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

# This is used to "warm up" the AWS meta data API.
# We were seeing > 5 secs. on the first call after
# starting an instance. Successive calls were
# returned _much_ faster.
def ping_aws_meta_data_api():
    url = 'http://169.254.169.254/latest/meta-data/'
    try:
        urllib2.urlopen(url, timeout = 10)
    except Exception as e: print(e)
