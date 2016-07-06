import math

ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
chunks_names = ['', 'thousand', 'million', 'billion', 'trillion']


def split_up(num):
    """
    Splits number into chunks of three
    """
    rev = str(math.floor(num))[::-1]
    chunks = []
    counter = 0
    current_chunk = ''
    for count, n in enumerate(rev, 1):
        if counter == 3:
            chunks.insert(0, current_chunk[::-1])
            counter = 0
            current_chunk = ''
        current_chunk += n
        counter += 1
        if count == len(rev):
            chunks.insert(0, current_chunk[::-1])
    return chunks


def hundreds_function(num):
    """expects a string of numbers"""
    ret = ''
    if len(num) == 1 and num == '0':
            return 'zero'
    if len(num) == 3:
        for count, n in enumerate(num, 1):
            if n == '0':
                if count == 3 and ret.endswith('-'):
                    ret = ret[:-1]
                continue

            if count == 1:
                ret += ones[int(n)] + " hundred"
            if count == 2:
                if n == '1':
                    ret += " and " + teens[int(num[2])]
                    return ret
                else:
                    ret += " and " + tens[int(n)] + "-"
            if count == 3:
                if num[0] == '0':
                    ret += " " + ones[int(n)]
                    continue
                ret += " and " + ones[int(n)] if not ret.endswith('-') else ones[int(n)]
    if len(num) == 2:
        for count, n in enumerate(num, 1):
            if n == '0':
                continue
            if count == 1:
                if n == '1':
                    ret += teens[int(num[1])]
                    return ret
                else:
                    ret += tens[int(n)]
            if count == 2:
                ret += "-" + ones[int(n)]
    if len(num) == 1:
        ret += ones[int(num)]
    return ret


def say(num):
    """
    Converts number between 0 and 1 trillion minus 1 to english words
    """
    if not 0 <= num < 1e12:
        raise AttributeError()
    split_list = split_up(num)
    ret = ''
    ret_list = []
    for n, chunk in enumerate(reversed(split_list)):
        try:
            chunk_name = chunks_names[n-1]
            if ret.strip().startswith(chunk_name) and chunk_name is not '':
                ret = ret.replace(chunk_name, '')
        except IndexError:
            pass
        if not ret.startswith(" "):
            ret_list.insert(0, hundreds_function(chunk) + " " + chunks_names[n] + " ")
        else:
            ret_list.insert(0, hundreds_function(chunk) + " " + chunks_names[n] + ret)

    for n, chunk in enumerate(ret_list, 1):
        if chunk.strip() in chunks_names:
            continue
        if n == len(ret_list):
            if (not ret.strip().endswith('and')
                    and any(cn in ret for cn in chunks_names[1:])):
                ret += "and"
        ret += chunk

    return ' '.join([x for x in ret.strip().split(' ') if x is not ''])

print(say(6000000008))
