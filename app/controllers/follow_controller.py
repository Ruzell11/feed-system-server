from app.services.follow_service import FollowService


async def follow_user_controller(db, user_id: int, target_id: int):
    return await FollowService.follow_user(db, user_id, target_id)


async def unfollow_user_controller(db, user_id: int, target_id: int):
    return await FollowService.unfollow_user(db, user_id, target_id)


async def get_followers_controller(db, user_id: int):
    return await FollowService.get_followers(db, user_id)


async def get_following_controller(db, user_id: int):
    return await FollowService.get_following(db, user_id)