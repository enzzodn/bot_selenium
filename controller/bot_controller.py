from model.wiki import wiki
from model.enviar_email import enviar_email
from model.remove import remove

txt1,txt2 = wiki()
# remove()
enviar_email(txt1, txt2)