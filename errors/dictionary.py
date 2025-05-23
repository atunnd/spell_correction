
NEAR_KEYS = {
    'a': ['q', 'w', 's', 'z'],
    'b': ['v', 'g', 'h', 'n'],
    'c': ['x', 'd', 'f', 'v'],
    'd': ['s', 'e', 'r', 'f', 'x', 'c'],
    'e': ['w', 's', 'd', 'r'],
    'f': ['d', 'r', 't', 'g', 'c', 'v'],
    'g': ['f', 't', 'y', 'h', 'v', 'b'],
    'h': ['g', 'y', 'u', 'j', 'b', 'n'],
    'i': ['u', 'j', 'k', 'o'],
    'j': ['h', 'u', 'i', 'k', 'n', 'm'],
    'k': ['j', 'i', 'o', 'l', 'm'],
    'l': ['k', 'o', 'p'],
    'm': ['n', 'j', 'k'],
    'n': ['b', 'h', 'j', 'm'],
    'o': ['i', 'k', 'l', 'p'],
    'p': ['o', 'l'],
    'q': ['a', 's', 'w'],
    'r': ['e', 'd', 'f', 't'],
    's': ['a', 'q', 'w', 'e', 'd', 'z', 'x'],
    't': ['r', 'f', 'g', 'y'],
    'u': ['y', 'h', 'j', 'i'],
    'v': ['c', 'f', 'g', 'b'],
    'w': ['q', 'a', 's', 'e'],
    'x': ['z', 's', 'd', 'c'],
    'y': ['t', 'g', 'h', 'u'],
    'z': ['a', 's', 'x']
}

tone_dict = {
    'á': ('a', 's'), 'à': ('a', 'f'), 'ả': ('a', 'r'), 'ã': ('a', 'x'), 'ạ': ('a', 'j'),
    'ắ': ('aw', 's'), 'ằ': ('aw', 'f'), 'ẳ': ('aw', 'r'), 'ẵ': ('aw', 'x'), 'ặ': ('aw', 'j'),
    'ấ': ('aa', 's'), 'ầ': ('aa', 'f'), 'ẩ': ('aa', 'r'), 'ẫ': ('aa', 'x'), 'ậ': ('aa', 'j'),
    'é': ('e', 's'), 'è': ('e', 'f'), 'ẻ': ('e', 'r'), 'ẽ': ('e', 'x'), 'ẹ': ('e', 'j'),
    'ế': ('ee', 's'), 'ề': ('ee', 'f'), 'ể': ('ee', 'r'), 'ễ': ('ee', 'x'), 'ệ': ('ee', 'j'),
    'í': ('i', 's'), 'ì': ('i', 'f'), 'ỉ': ('i', 'r'), 'ĩ': ('i', 'x'), 'ị': ('i', 'j'),
    'ó': ('o', 's'), 'ò': ('o', 'f'), 'ỏ': ('o', 'r'), 'õ': ('o', 'x'), 'ọ': ('o', 'j'),
    'ố': ('oo', 's'), 'ồ': ('oo', 'f'), 'ổ': ('oo', 'r'), 'ỗ': ('oo', 'x'), 'ộ': ('oo', 'j'),
    'ớ': ('ow', 's'), 'ờ': ('ow', 'f'), 'ở': ('ow', 'r'), 'ỡ': ('ow', 'x'), 'ợ': ('ow', 'j'),
    'ú': ('u', 's'), 'ù': ('u', 'f'), 'ủ': ('u', 'r'), 'ũ': ('u', 'x'), 'ụ': ('u', 'j'),
    'ứ': ('uw', 's'), 'ừ': ('uw', 'f'), 'ử': ('uw', 'r'), 'ữ': ('uw', 'x'), 'ự': ('uw', 'j'),
    'ý': ('y', 's'), 'ỳ': ('y', 'f'), 'ỷ': ('y', 'r'), 'ỹ': ('y', 'x'), 'ỵ': ('y', 'j'),
    'ô': ('o', 'o'), 'đ': ('d', 'd')
}

tone_dict_vni = {
    'á': ('a', '1'), 'à': ('a', '2'), 'ả': ('a', '3'), 'ã': ('a', '4'), 'ạ': ('a', '5'),
    'ắ': ('a8', '1'), 'ằ': ('a7', '2'), 'ẳ': ('a7', '3'), 'ẵ': ('a7', '4'), 'ặ': ('a7', '5'),
    'ấ': ('a6', '1'), 'ầ': ('a6', '2'), 'ẩ': ('a6', '3'), 'ẫ': ('a6', '4'), 'ậ': ('a6', '5'),
    'é': ('e', '1'), 'è': ('e', '2'), 'ẻ': ('e', '3'), 'ẽ': ('e', '4'), 'ẹ': ('e', '5'),
    'ế': ('e6', '1'), 'ề': ('e6', '2'), 'ể': ('e6', '3'), 'ễ': ('e6', '4'), 'ệ': ('e6', '5'),
    'í': ('i', '1'), 'ì': ('i', '2'), 'ỉ': ('i', '3'), 'ĩ': ('i', '4'), 'ị': ('i', '5'),
    'ó': ('o', '1'), 'ò': ('o', '2'), 'ỏ': ('o', '3'), 'õ': ('o', '4'), 'ọ': ('o', '5'),
    'ố': ('o6', '1'), 'ồ': ('o6', '2'), 'ổ': ('o6', '3'), 'ỗ': ('o6', '4'), 'ộ': ('o6', '5'),
    'ớ': ('o7', '1'), 'ờ': ('o7', '2'), 'ở': ('o7', '3'), 'ỡ': ('o7', '4'), 'ợ': ('o6', '5'),
    'ú': ('u', '1'), 'ù': ('u', '2'), 'ủ': ('u', '3'), 'ũ': ('u', '4'), 'ụ': ('u', '5'),
    'ứ': ('u7', '1'), 'ừ': ('u7', '2'), 'ử': ('u7', '3'), 'ữ': ('u7', '4'), 'ự': ('u7', '5'),
    'ý': ('y', '1'), 'ỳ': ('y', '2'), 'ỷ': ('y', '3'), 'ỹ': ('y', '4'), 'ỵ': ('y', '5'),
    'â': ('a', '6'), 'ă': ('a', '8'), 'ê': ('e', '6'), 'ô': ('o', '6'), 'ơ': ('o', '7'),
    'ư': ('u', '7'), 'đ': ('d', '9')
}