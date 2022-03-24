# Initialize the main Twitter class

class Twitter():
    """
    The Twitter class create a Twitter-like object that allows the user to write a tweet, create a tweeter thread, and have answers connected cascading down from the first tweet.
    """

    class TwitterThread():
        """
        Create the structure of a Twitter thread as a linked list
        """
        class Tweet():
            """
            Create the structure of the Tweet. It will have a string with the tweet, the pointer to the next tweet, and the pointer to the previous tweet.
            """
            def __init__(self, data:str, username):
                self.next = None
                self.prev = None
                self.tweet  = data
                self.username = username

            def __str__(self):
                """
                Graphical representation of the tweet
                """
                return f"'{self.tweet}' created by {self.username}"

        def __init__(self):
            """
            Initialize the Twitter object as a linked list
            """
            self.head = None
            self.tail = None
        
        def new_thread(self, tweet, username):
            new_tweet = Twitter.TwitterThread.Tweet(tweet, username)

            # Case 1 - List is empty
            if self.head == None:
                self.head = new_tweet
                self.tail = new_tweet

            # Case 2 - List is not empty
            else:
                new_tweet.next = self.head
                self.head.prev = new_tweet
                self.head = new_tweet

        def answer_tweet(self, tweet, username):
            new_tweet = Twitter.TwitterThread.Tweet(tweet, username)

            # Case 1 - List is empty
            if self.tail == None and self.head == None:
                self.head = new_tweet
                self.tail = new_tweet

            # Case 2 - List is not empty
            new_tweet.prev = self.tail
            self.tail.next = new_tweet
            self.tail = new_tweet
        
        def __str__(self):
            """
            Graphical representation of a twitter thread
            """
            output = "twitter-thread["
            first = True
            for value in self:
                if first:
                    first = False
                else:
                    output += ", "
                output += str(value)
            output += "]"
            return output    

        def __iter__(self):
            """
            Iterate forward through the twitter thread
            """
            # Start at the beginning of the thread
            curr = self.head
            while curr is not None:
                # Return a tweet to the user
                yield curr.tweet
                # Go to the next tweet
                curr = curr.next
    
    def __init__(self):
        """
        Create a list holding all the TwitterThread objects
        """
        self.twitter = []
      
    def add_new_thread(self, twitter_thread):
        """
        Add a TwitterThread object to the list
        """
        self.twitter.append(twitter_thread)
        print("Thread added successfuly")
        return 0

    def print_thread(self):
        """
        Print each TwitterThread object
        """
        for thread in self.twitter:
            print(thread)
            print()

# Test Cases
twitter = Twitter()
new_thread = twitter.TwitterThread()
tweet_1 = new_thread.Tweet("Hello World", "federico")
print(tweet_1) # 'Hello World' created by federico
new_thread.new_thread(tweet_1, "federico")
print(new_thread) # twitter-thread['Hello World' created by federico]
twitter.add_new_thread(new_thread) # Thread added successfuly
twitter.print_thread() # twitter-thread['Hello World' created by federico]
tweet_2 = new_thread.Tweet("Hello to you", "luca")
new_thread.answer_tweet(tweet_2, "luca")
print(new_thread) # twitter-thread['Hello World' created by federico, 'Hello to you' created by luca]