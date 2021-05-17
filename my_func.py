def input_int(msg_enter, limit = 5):
    input_cnt = 0
    res = None
    while input_cnt < limit:
        res = input(msg_enter)
        res = res if res.isdigit() else None

        if res is not None:
            res = int(res)
            break

        input_cnt += 1

    return res
