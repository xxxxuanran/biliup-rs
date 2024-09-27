import stream_gears


class Segment:
    pass


if __name__ == '__main__':
    segment = Segment()
    # segment.time = 60
    # segment.size = 6000 * 1024 * 1024
    segment.size = 60 * 1024 * 1024

    url = "https://live-global-cdn-v02.afreecatv.com/live-stmc-22/auth_playlist.m3u8?aid=.A32.7bbT56vyHM9fKZk.H-BM2W3YuuBlm8C46rvXXhU2NzpaS1FBptAdxkFSDPaYiJIuYMXJScGuHi1QPu53yh2YuzjgwhIGkJQ0XLB5P8OMy_oMyhbFdSCzLARwvtM"
    fake_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    }
    stream_gears.download(
        url=url,
        header_map=fake_headers,
        file_name="test%Y-%m-%dT%H_%M_%S",
        segment=segment
    )