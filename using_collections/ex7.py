#%%
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

parts = info.split(':')
print('+'.join(parts))

print(info.replace(":","+"))
# %%
