class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        print(secret, guess)
        s_len = len(secret)

        secret_ele = list(secret)
        guess_ele = list(guess)

        bulls_cnt = 0
        cows_cnt = 0

        for idx, ele in enumerate(guess_ele):
            if ele == secret_ele[idx]:
                bulls_cnt += 1
                guess_ele[idx] = '$'
                secret_ele[idx] = '$'

        for idx, ele in enumerate(guess_ele):
            if ele == '$':
                continue

            if ele in secret_ele:
                cows_cnt += 1
                secret_ele[secret_ele.index(ele)] = '$'

        str_result = "{}A{}B".format(bulls_cnt, cows_cnt)

        return str_result        