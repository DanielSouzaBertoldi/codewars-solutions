def make_readable(seconds):
    return "{:02d}:{:02d}:{:02d}".format(int(seconds / 3600), int((seconds / 60) % 60), int(seconds % 60));