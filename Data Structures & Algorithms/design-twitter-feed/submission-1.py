from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.follows = defaultdict(set) # uid -> {id of users they follow}
        self.tweets = defaultdict(list) # uid -> {tweets in insertion order}
        self.timestamp = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follows[userId].add(userId)
        self.tweets[userId].append((tweetId, self.timestamp))
        self.timestamp += 1        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.follows[followerId].discard(followeeId)
    
    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        # across all the follows, need to identify the top 10 greatest timestamps.
        # initialize heap with entries for each follows
        for follow_id in self.follows[userId]:
            tweets = self.tweets[follow_id]
            for tweet_id, timestamp in reversed(tweets):
                pos = len(tweets) - 1
                heap.append((-timestamp, tweet_id, follow_id, pos))
                break # just add the top one if any
            
        # now pop the top and replace any entry with next if any.
        heapq.heapify(heap) 
        ans = []
        while heap and len(ans) < 10:
            (_, tid, fid, pos) = heapq.heappop(heap)
            ans.append(tid)
            if pos > 0:
                pos -= 1
                ntid, ntime = self.tweets[fid][pos]
                heapq.heappush(heap, (-ntime, ntid, fid, pos)) 
            # else no longer need to track this fid
            
        return ans
        

        # analysis: all write operations are O(1), hash bases sets or append.
        # space needed is also O(1) per action.
        # newsfeed operations: O(# followees) initial load and heapify 
        # + up to 10 pop + push operations. O( timeline size * log (# followees) )
        # space: O(# followees) + timeline size.



            




