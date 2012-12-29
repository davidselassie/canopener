canopener
=========

Python convenience function `canopener(filename, mode='r')` for opening files.

Local files behave identically to `open()`.
```python
canopener('local_file.txt')
```

URLs can also be passed as the filename and opened for reading. `urllib2.urlopen()` is used under the covers, so it has equivalent support.
```python
canopener('http://remote/file.txt')
```

S3 URLs can also be read if the [boto](https://github.com/boto/boto) module is installed and the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY environment variables are set. The file is downloaded to a temporary local file on open.
```python
os.environ['AWS_ACCESS_KEY_ID'] = 'key'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'secret'
canopener('s3://bucket/file.txt')
```

Any paths with ".gz" or ".bz2" extensions are transparently decompressed.
```python
canopener('local_file.txt.gz')
canopener('local_file.txt.bz2')
canopener('http://remote/file.txt.gz')
canopener('s3://bucket/file.txt.gz')
```

There's also transparent compression when writing to local files.
```python
canopener('local_file.txt.gz', 'w')
```
