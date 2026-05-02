from app.repositories.follow_repository import FollowRepository


class FollowService:

    @staticmethod
    async def follow_user(db, follower_id: int, following_id: int):

        if follower_id == following_id:
            return {"message": "You cannot follow yourself"}
        return await FollowRepository.follow(db, follower_id, following_id)

    @staticmethod
    async def unfollow_user(db, follower_id: int, following_id: int):
        return await FollowRepository.unfollow(db, follower_id, following_id)

    @staticmethod
    async def get_followers(db, user_id: int):
        return await FollowRepository.get_followers(db, user_id)

    @staticmethod
    async def get_following(db, user_id: int):
        return await FollowRepository.get_following(db, user_id)