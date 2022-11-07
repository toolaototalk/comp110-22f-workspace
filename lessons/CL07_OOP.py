"""Examples of a class and objects."""

class Profile:
    handle: str
    followers: int
    is_private: bool

    def __init__(self, handle: str) -> None:
        """Initializing attributes."""
        self.handle = handle
        self.followers = 0
        self.is_private = False
        pass

    def tweet(self, msg: str) -> None:
        """Method example."""
        print(f"@{self.handle} tweets {msg}")

Leo_profile: Profile = Profile("Leo")
Leo_profile.tweet("Good morning.")


