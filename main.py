
# Python

from uuid import UUID
from datetime import date, datetime
from typing import Optional,List

# Pydantic

from pydantic import BaseModel
from pydantic import EmailStr 
from pydantic import Field

# FastAPI

from fastapi import FastAPI,status



app = FastAPI()


#Models

class UserBase(BaseModel):
    user_id: UUID = Field(...)
    email: EmailStr = Field(...)

class UserLogin(UserBase):
    password: str = Field(
        ...,
        min_length=8,
        max_length=64,
    )

class User(UserBase):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50,
    )
    date_of_birth: Optional[date] = Field(default=None)

class Tweet(BaseModel):
    tweet_id:UUID = Field(...)
    content: str = Field(
        ...,
        max_length=256,
        min_length=1
    )
    created_at: datetime = Field(default=datetime.now())
    update_at:  Optional [datetime] = Field(default=None)
    by: User = Field(...)



# Path Operations 

@app.get(path='/')
def home():
    return {'Twitter API': 'Working' }


## Users

@app.post(
    path = '/signup',
    response_model=User,
    status_code= status.HTTP_201_CREATED,
    summary= 'Register an User',
    tags= ['Users'],
)

def signup():
    pass


@app.post(
    path = '/login',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary= 'Login an User',
    tags= ['Users'],
)

def login():
    pass


@app.get(
    path = '/users',
    response_model=List[User],
    status_code= status.HTTP_200_OK,
    summary= 'Show all Users',
    tags= ['Users'],
)

def show_all_users():
    pass


@app.get(
    path = '/users/{user_id}',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary= 'Show an User',
    tags= ['Users'],
)

def show_an_user():
    pass


@app.delete(
    path = '/users/{user_id}/delete',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary= 'Delete an User',
    tags= ['Users'],
)

def delete_an_user():
    pass


@app.put(
    path = '/users/{user_id}/update',
    response_model=User,
    status_code= status.HTTP_200_OK,
    summary= 'Update an User',
    tags= ['Users'],
)

def update_an_user():
    pass

## Tweets
