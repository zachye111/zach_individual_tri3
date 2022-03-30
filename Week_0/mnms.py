
class mnms:
    def ur(self, small, big, goal):
        if goal >= 5 * big:
            remainder = goal - 5 * big
        else:
            remainder = goal % 5

        if remainder-small > 0:
            print(-1)
        else:
            print(remainder)


def myur():
    myurobj = mnms()
    myurobj.ur(2, 3, 17)
    myurobj.ur(9, 1, 14)

if __name__ == "__main":
    myur()
