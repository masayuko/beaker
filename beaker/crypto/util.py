from warnings import warn
from beaker import util


try:
    # Use PyCrypto (if available)
    from Crypto.Hash import HMAC as hmac, SHA as hmac_sha1
    sha1 = hmac_sha1.new

except ImportError:

    # PyCrypto not available.  Use the Python standard library.
    import hmac

    # When using the stdlib, we have to make sure the hmac version and sha
    # version are compatible
    # NOTE: We have to use the callable with hashlib (hashlib.sha1),
    # otherwise hmac only accepts the sha module object itself
    from hashlib import sha1
    hmac_sha1 = sha1
