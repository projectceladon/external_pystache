import pystache

def rot(s, n=13):
    r = ""
    for c in s:
        cc = c
        if cc.isalpha():
            cc = cc.lower()
            o = ord(cc)
            ro = (o+n) % 122
            if ro == 0: ro = 122
            if ro < 97: ro += 96
            cc = chr(ro)
        r = ''.join((r,cc))
    return r

def replace(subject, this='foo', with_this='bar'):
    return subject.replace(this, with_this)

class Lambdas(pystache.View):
    template_path = 'examples'
    
    def test(self):
        return 'laaa'

    def replace_foo_with_bar(self, text=None):
        return replace

    def rot13(self, text=None):
        return rot

    def sort(self, text=None):
        return lambda text: ''.join(sorted(text))
