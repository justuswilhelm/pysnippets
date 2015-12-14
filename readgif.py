from struct import unpack


def read_header(contents, start=0, end=6):
    r"""
    >>> read_header(b"\x47\x49\x46\x38\x39\x61")
    {'version': b'89a', 'signature': b'GIF'}
    """
    header = contents[start:end]
    signature = header[:3]
    version = header[3:]
    assert signature == b"GIF"
    assert version in [b'89a', b'87a']
    return {'signature': signature, 'version': version}


def read_logical_screen_descriptor(contents, start=6, end=13):
    def read_packed_field(packed):
        packed = bin(packed)[2:]
        global_color_table_flag = bool(packed[0])
        sort_flag = bool(packed[4])
        color_resolution = int(packed[1:4], 2)
        global_color_table_size = 2 ** (1 + int(packed[5:], 2))
        return {
            'global_color_table_flag': global_color_table_flag,
            'sort_flag': sort_flag,
            'color_resolution': color_resolution,
            'global_color_table_size': global_color_table_size,
        }

    width, height, packed, background_color_index, aspect_ratio = unpack(
        "HHBBB", contents[start:end])
    result = {
        'width': width, 'height': height, 'aspect_ratio': aspect_ratio,
        'background_color_index': background_color_index,
    }
    result.update(read_packed_field(packed))
    return result


def read_global_color_table(contents, size, start=13):
    global_color_table_raw = contents[start:(3 * size) + start]
    global_color_table = {}
    for color_index, global_color in enumerate(range(size)):
        global_color_table[color_index] = [
            ord(val) for val in global_color_table_raw[
                color_index * 3: 3 * color_index + 3]]
    return global_color_table

if __name__ == "__main__":
    with open("test.gif", "rb") as fd:
        contents = fd.read()
    header = read_header(contents)
    logical_screen_descriptor = read_logical_screen_descriptor(contents)
    if logical_screen_descriptor['global_color_table_flag']:
        global_color_table = read_global_color_table(
            contents,
            logical_screen_descriptor['global_color_table_size'],
        )
