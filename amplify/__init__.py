from hch import HCH
from meta import Meta, StatelessMeta
from reliability import amplify_reliability

def amplify(A):
    return Meta(HCH(amplify_reliability(A)))

def stateless_amplify(A):
    return StatelessMeta(HCH(amplify_reliability(A)))
