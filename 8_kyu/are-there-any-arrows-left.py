
'''https://www.codewars.com/kata/559f860f8c0d6c7784000119/train/python'''


def any_arrows(arrows):
    return False in [x.get('damaged',False) for x in arrows]