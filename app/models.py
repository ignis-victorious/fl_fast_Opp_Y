#
#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#  ______________________


class AddRequest(BaseModel):
    a: int
    b: int
