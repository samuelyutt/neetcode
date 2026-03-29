class Twitter:

    def __init__(self):
        self.follow_record = defaultdict(set)
        self.post_record = defaultdict(list) # user -> [(idx, postId)]
        self.post_idx = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.post_record[userId].append((self.post_idx, tweetId))
        self.post_idx += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        users = list(self.follow_record[userId]) + [userId]
        posts = []
        for u in users:
            posts += self.post_record[u]
        posts.sort()
        posts = [p for _, p in posts[-10:]]
        posts.reverse()
        return posts

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.follow_record[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_record[followerId].discard(followeeId)
