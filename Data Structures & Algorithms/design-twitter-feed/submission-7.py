class Twitter:

    def __init__(self):
        self.postCount = 0
        self.postByUser = {}  # q of 10 post per user
        self.MAX_RECENT_POST = 10
        self.followerToFollowee = {} # set of followee

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.postCount += 1
        ref = self.postByUser[userId] = self.postByUser.get(userId, deque([]))
        ref.append((self.postCount, tweetId))
        if len(ref) > self.MAX_RECENT_POST: ref.popleft()

    def getNewsFeed(self, userId: int) -> List[int]:
        followers = self.followerToFollowee[userId] = self.followerToFollowee.get(userId, set())
        followers.add(userId)
        feed = []
        for follower in followers:
            for post in self.postByUser.get(follower, []):
                heapq.heappush(feed, (-post[0], post[1]))
        res = []
        for _ in range(min(len(feed), self.MAX_RECENT_POST)):
            res.append(heapq.heappop(feed)[1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        ref = self.followerToFollowee[followerId] = self.followerToFollowee.get(followerId, set())
        ref.add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        ref = self.followerToFollowee[followerId] = self.followerToFollowee.get(followerId, set())
        if followeeId in ref: ref.remove(followeeId)
