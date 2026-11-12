import json
from text_ascii_audit import transform
def test_transform():
    value='é'
    if True: result=transform(value)
    else: result=transform(json.loads(value))
    assert 'U+00E9' in json.dumps(result,ensure_ascii=False)
