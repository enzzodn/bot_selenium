from model.wiki import wiki
from model.enviar_email import enviar_email

txt1,txt2 = wiki()
enviar_email(txt1, txt2)