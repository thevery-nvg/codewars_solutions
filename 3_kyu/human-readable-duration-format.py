
'''https://www.codewars.com/kata/52742f58faf5485cae000b9a/train/python'''


def format_duration(seconds):
    from collections import defaultdict
    if seconds == 0:
        return 'now'
    times = {'year': 31536000, 'day': 86400, 'hour': 3600, 'minute': 60, 'second': 1}
    res = defaultdict(int)
    for t in times.keys():
        while seconds // times[t] != 0:
            seconds -= times[t]
            res[t] += 1
    if len(res) == 1:
        res = list(res.items())
        s = 's' if res[0][1]>=2 else ''
        return str(res[0][1])+' '+str(res[0][0]+s)
    last = list(res.keys())[-1]
    out = ''
    for k in res:
        s = '' if res[k] < 2 else 's'
        if k != last:
            # s = '' if res[k]<2 else 's'
            out += str(res[k])+' '+ k+s+', '
        else:
            out = out.strip(', ')
            out +=' and '+str(res[last])+ ' ' +last+s
    return out