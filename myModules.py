# Generating id
import string as st
import random

def idGenerator(length):
    all_Characters = (st.ascii_uppercase + st.digits)
    id_chars = random.sample(all_Characters,k=length)

    id = "".join(id_chars)
    return id
