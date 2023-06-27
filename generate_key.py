import pickle
from pathlib import Path



import streamlit_authenticator as sauth

names = ["Omowaye Victor", "vee"]
username = ["Omov", "eve"]
password = ["XXX", "XXX"]

hashed_passwords = sauth.Hasher(password).generate()

file_path = Path(__file__).parent / "hashed_pw.pk1"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords,file)