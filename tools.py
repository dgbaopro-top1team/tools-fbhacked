import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))