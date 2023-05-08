[[COMP26020]]

### opening files
`open` creates a reference to a file - **a file descriptor**. 
```C
int open(const char *pathname, int flags, mode_t mode)
```
- `*pathname` - path of the file
- `flags`
	- Access mode: `O_RDONLY`, `O_WRONLY`, `O_RDWR`
	- Create file if it doesn't exist: `O_CREATE`
	- Truncate the file size to 0 if exists: `O_TRUNC`
- `mode` - file permissions if the file is created

example
```C
int file_descriptor = open("/home/bunmi/test", O_RDWR | O_CREAT, S_IRWXU);
```

### reading files
`read` attempts to read bytes from a file, given a **file descriptor**
```C
ssize_t read(int fd, void *buf, size_t count);
```
- `fd` - the file descriptor (made with `open`)
- `buf` - the address of the buffer that receives the content being read
- `count` - the number of bytes that should be read
`read` returns the number of bytes that actually end up being read

example
```C
int bytes_read = read(file_descriptor, buffer, 10);
if (bytes_read == -1) //error
else if (bytes_read != 10) //whatever
```

### writing to files
`write` attempts to write bytes to a file from a given buffer, to the given **file descriptor**

example
```C
int bytes_written = write(file_descriptor, buffer, 10);
if (bytes_written == -1) //error
else //whatever
```

once you are finished writing to a file, use `close`
```C
int close(int fd)
```

### generating random numbers
`rand()` will return any random number between 0 and `RAND_MAX` - to get values between 0 and other values, simply do `rand()%max` where `max` is the (non inclusive) upper bound you want to generate between

random sequences will always be the same, so in order to generate *random* random sequences, you can generate a seed based on the current time:
`srand(time(NULL));`

### <span style="font-family:t">strtol</span>
`atoi` is very easy to use, but when the string is malformed / out of integer bounds, problems can occur as `atoi` doesn't offer any way to detect when things like this occur

solution: use `strtol`
```C
long strtol(const char *nptr, char **endptr, int base);
```
- `*nptr` is converted to a long integer, and returned
- `base` can be specified (10 for decimal obviously)
- `**endptr` points to the first invalid character of the string, or `\0` if the string is fully valid
- under/overflows cause `errno` to be set to `ERANGE`, and the function returns `LONG_MIN` / `LONG_MAX` for underflow / overflow

### stream based file io
```C
FILE *fopen(const char *pathname, const char *mode);
```
`FILE` is a stream object which is returned by `fopen`
- `pathname` - the path for the file to open
- `mode`
	- `r` = read-only
	- `r+` = read-write
	- `w` = write-only + truncate/create
	- `w+` = read-write + truncate/create
use `fclose(FILE *stream);` to close the stream

to read from streams:
```C
size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream);
```

to write to streams:
```C
size_t fwrite(const void *ptr, size_t size, size_t nmemb, FILE *stream);
```

- `nmemb` - no of contiguous items to read
- `size` - size of each item mentioned above (in **bytes**)
- `stream` - the stream object
- `ptr` - the location to read to / write from
both functions return the number of items read/written