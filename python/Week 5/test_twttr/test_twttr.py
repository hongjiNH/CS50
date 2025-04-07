from twttr import shorten

def test():
    assert shorten("hmma")=="hmm"
    assert shorten("sequoia")=="sq"
    assert shorten("rhythm1")=="rhythm1"
    assert shorten("H,ELLO")=="H,LL"
