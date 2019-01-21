import base64
from pathlib import Path

import cv2


HTML_TEMPLATE = """
<html>
<body>
<img src="{}">
</body>
</html>
"""


def main():
    path = Path("lena.png")
    img = cv2.imread(str(path), cv2.IMREAD_COLOR)
    src = ndarray2base64(img, path.suffix)
    embeded = HTML_TEMPLATE.format(src)
    with open("dst.html", 'w') as f:
        f.write(embeded)


def ndarray2base64(ndarray, suffix):
    """ np.ndarrayをhtmlのimgのsrcに埋め込める形に変換
    """
    TEMPLATE = "data:image/{};base64,{}"

    _, encoded = cv2.imencode(suffix, ndarray)

    # base64にエンコードした際の b'~~~' というフォーマットの内、不要な部分を除く
    b64img = str(base64.b64encode(encoded))[2:-1]
    # pathlib.Path.suffixの先頭に含まれる'.'を除去
    ext = suffix[1:]

    return TEMPLATE.format(ext, b64img)


if __name__ == '__main__':
    main()
