# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field, Extra


DEFAULT_TITLE = DEFAULT_ARTIST_NAME = DEFAULT_ALBUM_NAME = 'Unknown'


class Common(BaseModel):
    class Config:
        allow_population_by_field_name = True
        extra = Extra.ignore

    duration: float
    title: str = DEFAULT_TITLE

    artists_name: str = Field(DEFAULT_ARTIST_NAME, alias='artist')
    album_name: str = Field(DEFAULT_ALBUM_NAME, alias='album')
    album_artist_name: str = Field(DEFAULT_ARTIST_NAME, alias='albumartist')

    track: str = Field('1/1', alias='tracknumber')
    disc: str = Field('1/1', alias='discnumber')

    date: str = ''
    genre: str = ''


class EasyMP3Model(Common):
    pass


class APEModel(Common):
    pass


class FLACModel(Common):
    track_number: int = Field(1, alias='tracknumber')
    disc_number: int = Field(1, alias='discnumber')
    track_total: int = Field(1, alias='tracktotal')
    disc_total: int = Field(1, alias='disctotal')
