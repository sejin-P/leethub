import collections

class Twitter:

    def __init__(self):
        self.followerList = {}
        self.postList = {}
        self.postCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        li = self.postList.get(userId)
        self.postCount += 1
        postNum = self.postCount
        if li is None:
            self.postList[userId] = [[tweetId, postNum]]
            return
        
        self.postList[userId].append([tweetId, postNum])
        return

    def getNewsFeed(self, userId: int) -> List[int]:
        followLi = self.followerList.get(userId)
        if followLi is None:
            followLi = []
        
        posts = self.postList.get(userId)
        if posts is None:
            posts = []
        posts = posts[:]
        for f in followLi:
            followeePosts = self.postList.get(f)
            if followeePosts is None:
                continue
            posts += followeePosts
        
        posts.sort(key = lambda x: x[1], reverse = True)
        
        return [post[0] for post in posts][:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        li = self.followerList.get(followerId)
        if li is None:
            self.followerList[followerId] = [followeeId]
            return
        
        if followeeId in li:
            return
        self.followerList[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        li = self.followerList.get(followerId)
        if li is None:
            return
        
        self.followerList[followerId].remove(followeeId)
        return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)