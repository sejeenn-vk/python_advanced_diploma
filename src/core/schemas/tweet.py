from pydantic import BaseModel, ConfigDict, Field


class Tweet(BaseModel):
    ...


class CreateTweet(Tweet):
    ...
