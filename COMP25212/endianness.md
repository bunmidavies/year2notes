[[COMP25212]]

- Little endian = least significant at the lowest address (i.e. 0 at the very right)
- Big endian = most significant at the lowest address (i.e. 0 at the very right)

Little endian in most applications is the more popular application

This will only ever get confusing if both are ==mixed== together, or data is trying to be transferred between different systems which make use of different endianness