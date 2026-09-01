import heapq
from collections import defaultdict

class Twitter(object):
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)  # userId -> list of (time, tweetId)
        self.following = defaultdict(set)  # userId -> set of followeeIds

    def postTweet(self, userId, tweetId):
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId):
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            tw = self.tweets[u]
            if tw:
                idx = len(tw) - 1
                t, tid = tw[idx]
                heapq.heappush(heap, (-t, tid, u, idx - 1))

        res = []
        while heap and len(res) < 10:
            negt, tid, u, idx = heapq.heappop(heap)
            res.append(tid)
            if idx >= 0:
                t, ntid = self.tweets[u][idx]
                heapq.heappush(heap, (-t, ntid, u, idx - 1))
        return res

    def follow(self, followerId, followeeId):
        if followerId != followeeId:
            self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna