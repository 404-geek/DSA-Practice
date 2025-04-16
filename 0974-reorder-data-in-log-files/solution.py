class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for log in logs:
            id_, rest = log.split(" ", 1)
            if rest[0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append((rest, id_))

        letter_logs.sort()

        letter_logs = [f"{id_} {rest}" for rest, id_ in letter_logs]

        return letter_logs + digit_logs

