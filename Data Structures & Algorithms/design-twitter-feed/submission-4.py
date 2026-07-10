class Twitter:

    def __init__(self):
        self.userFeed = defaultdict(list)
        self.userFollows = defaultdict(set)
        self.tweetCounter = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCounter+=1
        heapq.heappush(self.userFeed[userId],[self.tweetCounter*-1,tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        tempFeed =[x for x in self.userFeed[userId]]
        for followee in self.userFollows[userId]:
            tempFeed.extend(self.userFeed[followee])
        tempFeed = [x for x in tempFeed]
        
        heapq.heapify(tempFeed)
        final = tempFeed
        for x in range(len(final)):
            res.append((heapq.heappop(final)[1]))

        return res[:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.userFollows[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        elif followeeId in self.userFollows[followerId]:
            self.userFollows[followerId].remove(followeeId)

        
